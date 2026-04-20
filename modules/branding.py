import os

class BrandingModule:
    @staticmethod
    def get_icon_command(icon_path):
        """Memvalidasi dan memberikan perintah icon untuk PyInstaller"""
        if icon_path and os.path.exists(icon_path):
            # Pastikan filenya berakhiran .ico
            if icon_path.lower().endswith('.ico'):
                return f"--icon={icon_path}"
        return None

    @staticmethod
    def get_version_info():
        """Fitur Masa Depan: Menambahkan info versi Mr.Rm19 ke EXE"""
        return "1.0.0"
