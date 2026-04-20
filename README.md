
#  Web2Exe Builder - Professional Suite
**Developed by Mr.Rm19**

![Python](https://img.shields.io/badge/python-3.14+-green.svg)
![License](https://img.shields.io/badge/license-MIT-important.svg)

**Web2Exe Builder** adalah alat utilitas berbasis Python yang dirancang untuk mengonversi proyek web (HTML/JS/PHP) menjadi file executable (.exe) tunggal yang profesional. Dengan arsitektur modular, alat ini memungkinkan integrasi engine server portabel dan proteksi aset dalam satu klik.

---
<br><img src="https://raw.githubusercontent.com/Mister-RdanM19/Web2Exe/refs/heads/main/builder.png">

## 🌟 Fitur Unggulan

*   **Modular Architecture**: Fitur dipisahkan ke dalam modul khusus (`branding`, `php`, `security`) untuk stabilitas kode.
*   **Engine Integration**: Kemampuan membungkus `bin/php_dist` secara otomatis ke dalam paket aplikasi.
*   **Professional UI**: Antarmuka berbasis `CustomTkinter` dengan tema gelap dan log konsol ala hacker.
*   **Automated Workflow**: Mengotomatisasi penggunaan PyInstaller, pembersihan folder sampah, dan manajemen output.
*   **Branding Control**: Dukungan penuh untuk kustomisasi ikon (.ico) dan metadata aplikasi.

---

## 📂 Struktur Repositori

```text
Web2Exe_Project/
├── main.py                # Entry point & GUI Manager
├── ui_manager.py          # Logika Antarmuka (Resepsionis)
├── compiler_core.py       # Mesin Rakit Utama (Mekanik)
├── modules/               # Gudang Fitur (Modular)
│   ├── __init__.py        # Python Package Init
│   ├── php_module.py      # Integrasi Server Side
│   ├── branding.py        # Pengaturan Visual & Icon
│   └── security.py        # Protokol Keamanan & Enkripsi
├── templates/             # Kerangka Kerja (Templates)
│   └── wrapper.py         # Skrip Wrapper untuk webview
├── bin/                   # Binary Files (Alat Pendukung)
│   └── php_dist/          # Portabel PHP Environment
└── output/                # Destinasi Hasil Rakitan (.exe)

```

-----




## ⚖️ Disclaimer

Alat ini disediakan "sebagaimana adanya" untuk tujuan pengembangan dan produktivitas. Pengembang (**Mr.Rm19**) tidak bertanggung jawab atas penyalahgunaan alat ini untuk tujuan ilegal atau distribusi perangkat lunak tanpa izin. Gunakan dengan bijak dan patuhi kebijakan lisensi perangkat lunak yang Anda konversi.

---

## DEVELOPER 
* Mr.Rm19 - ramdan19id@gmail.com


**Copyright © 2026 Mr.Rm19 - Professional Tooling Suite.**

