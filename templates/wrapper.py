import webview
import os
import sys
import subprocess
import threading
import time

def get_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def start_php():
    # Path ke php.exe yang dibungkus
    php_exe = get_path("php/php.exe")
    # Path ke folder website
    web_root = get_path("www")
    
    # Jalankan PHP Built-in Server di port 8080
    if os.path.exists(php_exe):
        subprocess.Popen(
            [php_exe, "-S", "localhost:8080", "-t", web_root],
            creationflags=subprocess.CREATE_NO_WINDOW
        )

if __name__ == "__main__":
    # Jalankan PHP di thread terpisah
    threading.Thread(target=start_php, daemon=True).start()
    
    # Tunggu sebentar agar server siap
    time.sleep(2)
    
    # Buka jendela aplikasi mengarah ke localhost
    window = webview.create_window('Mr.Rm19 App', 'http://localhost:8080')
    webview.start()
