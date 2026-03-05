# manual_book_gab/models/manual_book.py
from odoo import models, fields, api

class ManualBookGAB(models.Model):
    _name = 'manual.book.gab'
    _description = 'Manual Book GAB'
    _order = 'sequence, id'

    name = fields.Char(string='Judul Panduan', required=True)
    sequence = fields.Integer(default=10)
    category = fields.Selection([
        ('frontend', 'Front End'),
        ('backend', 'Back End (Odoo)'),
        ('user_guide', 'Panduan User'),
        ('sop', 'SOP Perusahaan'),
    ], string='Kategori', default='user_guide', required=True)

    # Widget HTML untuk menulis konten dokumentasi (bisa insert gambar/tabel)
    content = fields.Html(string='Isi Dokumentasi', sanitize=False)
    
    author_id = fields.Many2one('res.users', string='Penulis', default=lambda self: self.env.user)
    date_published = fields.Date(string='Tanggal Terbit', default=fields.Date.context_today)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('review', 'Ditinjau'),
        ('published', 'Terbit'),
    ], string='Status', default='draft')

    def action_draft(self):
        for record in self:
            record.state = 'draft'

    def action_review(self):
        for record in self:
            record.state = 'review'

    def action_publish(self):
        for record in self:
            record.state = 'published'