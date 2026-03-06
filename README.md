# 🚀 Odoo Learning Project: Manual Book & Reporting System

Proyek ini adalah wadah belajar saya untuk mendalami pengembangan modul **Odoo (Backend & Frontend)**. Di sini saya fokus pada manajemen dokumen dan integrasi fitur laporan profesional.

## 📚 Apa yang Saya Pelajari di Sini?
  * **ORM Odoo**: Belajar cara kerja `models`, `fields`, dan `api.model` untuk manipulasi data di database PostgreSQL.
  * **Dynamic Reporting (PDF)**: Menggunakan **QWeb Template** untuk merender laporan PDF yang dinamis, termasuk logika perhitungan total harga menggunakan `t-set`.
  * **Excel Integration**: Implementasi library `xlsxwriter` di Python untuk menghasilkan file `.xlsx` asli dengan *styling* warna, logo, dan kalkulasi otomatis.
  * **UI/UX Design**: Merapikan tampilan Form dan Tree view, termasuk penggunaan `widget="badge"` dan `widget="monetary"`.
  * **State Management**: Belajar alur kerja status (*workflow*) dari `Draft` -> `Review` -> `Published`.
  * **Error Handling**: Menangani error teknis seperti `XML Syntax Error` (mismatch tag) dan `TypeError` (null values pada operasi matematika).

* ## Fitur Utama
  * **Manajemen Dokumentasi**: Membuat, mengedit, dan menyimpan konten panduan dalam format HTML.
  * **Penomoran Otomatis**: Menggunakan sequence untuk nomor referensi dokumen.
  * **Pelacakan Status (State)**: Alur kerja dokumen mulai dari `Draft`, `Ditinjau`, hingga `Terbit`.
  * **Manajemen Harga**: Field khusus untuk mencatat nilai atau harga pada setiap dokumen panduan.
  * **Reporting**:
      * **PDF**: Cetak ringkasan daftar panduan dengan total harga otomatis.
      * **Excel**: Download rekapitulasi data ke format `.xlsx` menggunakan library `xlsxwriter`, lengkap dengan logo perusahaan, filter status/kategori, dan perhitungan total harga.

 
## Struktur Modul
    
    manual_book_gab/
    ├── data/
    │   └── ir_sequence_data.xml         # Konfigurasi penomoran otomatis
    ├── models/
    │   └── manual_book_gab.py           # Logika utama dan definisi field
    ├── report/
    │   └── manual_book_report_views.xml # Template laporan PDF (QWeb)
    ├── security/
    │   └── ir.model.access.csv          # Pengaturan hak akses user
    ├── views/
    │   └── manual_book_views.xml        # Tampilan UI (Tree & Form View)
    ├── wizard/
    │   ├── manual_book_print_wizard.py  # Logika ekspor Excel (xlsxwriter)
    │   └── manual_book_print_wizard_view.xml # Tampilan popup cetak
    ├── __init__.py                      # Inisialisasi package Python
    └── __manifest__.py                  # Identitas dan konfigurasi modul

## Instalasi
1. Pastikan library `xlsxwriter` sudah terpasang:
     ```bash
     pip install xlsxwriter
2. Pastikan modul mail terpasang (untuk fitur chatter).
3. Masukkan folder modul ke direktori addons Odoo kamu.
4. Update Apps List dan Install/Upgrade modul GAB Manual Book.

## 💻 Cara Menjalankan (Docker Environment)
1. Clone repository ini.
2. Pastikan Docker sudah aktif di MacBook.
3. Jalankan perintah:
     ```bash
     docker compose up -d
4. Upgrade modul manual_book_gab untuk melihat perubahan terbaru.

5. 
Created with ❤️ by Ana Lativach

_Student @ Universitas Nahdlatul Ulama Yogyakarta_
