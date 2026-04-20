import os
import shutil
import subprocess
import sys
# Memanggil nyawa dari gudang fitur
from modules.php_module import PHPModule
from modules.branding import BrandingModule
from modules.security import SecurityModule

class CompilerEngine:
    def __init__(self, log_func):
        """
        Inisialisasi mesin compiler.
        log_func: fungsi untuk mengirim pesan ke terminal/GUI.
        """
        self.log = log_func

    def start_build(self, app_name, source_path, extra_configs=None):
        """
        Proses utama perakitan EXE menggunakan sistem modul.
        """
        try:
            self.log(f"--- MEMULAI RAKIT PRO: {app_name} ---")
            
            # 1. Setup Folder Kerja
            temp_dir = "build_temp"
            output_dir = "output"
            
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)
            
            os.makedirs(os.path.join(temp_dir, "www"))
            
            # 2. Validasi & Penyalinan Asset
            if not os.path.exists(source_path):
                raise Exception(f"Folder sumber tidak ditemukan: {source_path}")

            self.log("Menyalin asset website ke workspace...")
            shutil.copytree(source_path, os.path.join(temp_dir, "www"), dirs_exist_ok=True)
            
            # Pastikan template ada
            template_path = "templates/wrapper.py"
            if not os.path.exists(template_path):
                raise Exception("Template 'wrapper.py' tidak ditemukan!")
            
            shutil.copy(template_path, temp_dir)
            
            # 3. Konfigurasi Perintah PyInstaller (Memanggil Modul)
            self.log("Menghubungkan ke gudang fitur...")
            
            cmd = [
                "pyinstaller",
                "--onefile",
                "--noconsole",
                f"--name={app_name}",
                "--add-data=www;www", 
            ]

            # --- MENGGUNAKAN PHP MODULE ---
            if extra_configs and extra_configs.get('use_php'):
                php_args = PHPModule.get_php_args() # Memanggil logika dari modules/php_module.py
                if php_args:
                    cmd.append(php_args)
                    self.log("Integrasi Module: PHP Engine aktif.")
                else:
                    self.log("Peringatan: Folder PHP di bin/ tidak ditemukan.")

            # --- MENGGUNAKAN BRANDING MODULE (ICON) ---
            if extra_configs and 'icon_path' in extra_configs:
                # Memanggil logika dari modules/branding.py
                icon_cmd = BrandingModule.get_icon_command(extra_configs['icon_path'])
                if icon_cmd:
                    cmd.append(icon_cmd)
                    self.log(f"Integrasi Module: Icon berhasil dipasang.")

            # Menambahkan file script utama
            cmd.append("wrapper.py")

            # 4. Eksekusi Kompilasi
            self.log("Proses konversi ke EXE sedang berjalan... (Tunggu 1-2 menit)")
            
            process = subprocess.run(
                cmd, 
                cwd=temp_dir, 
                capture_output=True, 
                text=True, 
                shell=True
            )

            if process.returncode != 0:
                self.log("--- ERROR PYINSTALLER ---")
                self.log(process.stderr)
                raise Exception("Gagal merakit EXE.")

            # 5. Finalisasi
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            exe_path = os.path.join(temp_dir, "dist", f"{app_name}.exe")
            target_path = os.path.join(output_dir, f"{app_name}.exe")

            if os.path.exists(exe_path):
                if os.path.exists(target_path):
                    os.remove(target_path)
                
                shutil.move(exe_path, target_path)
                self.log(f"SUKSES TOTAL! File: {target_path}")
            else:
                raise Exception("Hasil rakitan tidak ditemukan.")
            
            return True

        except Exception as e:
            self.log(f"CRITICAL ERROR: {str(e)}")
            return False