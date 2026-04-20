import os

class PHPModule:
    @staticmethod
    def get_php_args():
        """Mengembalikan argumen PyInstaller untuk membungkus PHP"""
        # Sesuaikan dengan folder bin/php_dist kamu
        php_path = os.path.abspath("bin/php_dist")
        if os.path.exists(php_path):
            # Format: path_asal;nama_folder_di_dalam_exe
            return f"--add-data={php_path};php"
        return None