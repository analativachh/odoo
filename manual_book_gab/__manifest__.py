# manual_book_gab/__manifest__.py
{
    'name': 'GAB Manual Book',
    'version': '1.0',
    'category': 'Documentation',
    'summary': 'Sistem Manajemen Dokumentasi Internal GAB',
    'description': """
        Modul ini digunakan untuk menyimpan manual book, 
        SOP, dan panduan teknis bagi user GAB.
    """,
    'author': 'Ana Lativach',
    'depends': ['base', 'mail'], # base adalah dasar, web untuk fitur UI
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/manual_book_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}