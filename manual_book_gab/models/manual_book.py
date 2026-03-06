from odoo import models, fields, api, _

class ManualBookGAB(models.Model):
    _name = 'manual.book.gab'
    _inherit = ['mail.thread']
    _description = 'Manual Book GAB'
    _order = 'number desc, id desc'

    number = fields.Char(string='Nomor Referensi', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    name = fields.Char(string='Judul Panduan', required=True, tracking=True)
    sequence = fields.Integer(default=10)
    category = fields.Selection([
        ('frontend', 'Front End'),
        ('backend', 'Back End (Odoo)'),
        ('user_guide', 'Panduan User'),
        ('sop', 'SOP Perusahaan'),
    ], string='Kategori', default='user_guide', required=True, tracking=True)

    content = fields.Html(string='Isi Dokumentasi', sanitize=False, tracking=True)
    author_id = fields.Many2one('res.users', string='Penulis', default=lambda self: self.env.user, tracking=True)
    date_published = fields.Date(string='Tanggal Terbit', default=fields.Date.context_today, tracking=True)
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('review', 'Ditinjau'),
        ('published', 'Terbit'),
    ], string='Status', default='draft', tracking=True)

    @api.model
    def create(self, vals):
        if vals.get('number', _('New')) == _('New'):
            vals['number'] = self.env['ir.sequence'].next_by_code('manual.book.gab') or _('New')
        return super(ManualBookGAB, self).create(vals)
    
    # State Actions
    def action_draft(self):
        self.write({'state': 'draft'})

    def action_review(self):
        self.write({'state': 'review'})

    def action_publish(self):
        self.write({'state': 'published'})

    