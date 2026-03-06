import io
import base64
from odoo import models, fields, api
try:
    import xlsxwriter
except ImportError:
    xlsxwriter = None

class ManualBookPrintWizard(models.TransientModel):
    _name = 'manual.book.print.wizard'
    _description = 'Wizard Cetak Bukti'
    
    print_date = fields.Date(string='Tanggal Cetak', default=fields.Date.context_today)
    state_filter = fields.Selection([
        ('all', 'Semua Status'),
        ('draft', 'Draft'),
        ('review', 'Ditinjau'),
        ('published', 'Diterbitkan')
    ], string='Status', default='all')

    category_filter = fields.Selection([
        ('all', 'Semua Kategori'),
        ('user', 'Panduan User'),
        ('admin', 'Panduan Admin'),
        ('technical', 'Panduan Teknis')
    ], string='Kategori', default='all')

    date_from = fields.Date(string='Dari Tanggal')
    date_to = fields.Date(string='Sampai Tanggal')
    notes = fields.Text(string='Catatan Laporan')

    def _get_filtered_docs(self):
        domain = []
        if self.state_filter != 'all':
            domain.append(('state', '=', self.state_filter))
        if self.category_filter != 'all':
            domain.append(('category', '=', self.category_filter))
        if self.date_from:
            domain.append(('date_published', '>=', self.date_from))
        if self.date_to:
            domain.append(('date_published', '<=', self.date_to))
        return self.env['manual.book.gab'].search(domain)

    # TOMBOL PDF: Tetap panggil template tabel PDF kamu
    def action_confirm_print(self):
        docs = self._get_filtered_docs()
        return self.env.ref('manual_book_gab.action_report_manual_book_summary').report_action(docs)

    # TOMBOL EXCEL: Bikin file .xlsx beneran pake Python
    def action_print_excel(self):
        docs = self._get_filtered_docs()
        
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet('Rekapitulasi GAB')

        # Styling sederhana
        header_format = workbook.add_format({'bold': True, 'bg_color': '#D3D3D3', 'border': 1})
        border = workbook.add_format({'border': 1})

        # Header
        headers = ['Ref Number', 'Title', 'Category', 'Date Published', 'State']
        for col, header in enumerate(headers):
            sheet.write(0, col, header, header_format)

        # Isi Data
        row = 1
        for o in docs:
            sheet.write(row, 0, o.number or '', border)
            sheet.write(row, 1, o.name or '', border)
            sheet.write(row, 2, o.category or '', border)
            sheet.write(row, 3, str(o.date_published) if o.date_published else '', border)
            sheet.write(row, 4, o.state or '', border)
            row += 1

        workbook.close()
        output.seek(0)
        
        # Proses download file
        file_base64 = base64.b64encode(output.read())
        attachment = self.env['ir.attachment'].create({
            'name': 'Rekapitulasi_Manual_Book.xlsx',
            'type': 'binary',
            'datas': file_base64,
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        })

        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%s?download=true' % attachment.id,
            'target': 'new',
        }