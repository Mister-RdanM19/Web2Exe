import os

class BrandingModule:
    @staticmethod
    def get_icon_command(icon_path):
        """Mengembalikan perintah icon untuk PyInstaller jika file ada"""
        if icon_path and os.path.exists(icon_path):
            return f"--icon={icon_path}"
        return None

    @staticmethod
    def get_version_info(app_name, version):
        """Nantinya bisa digunakan untuk menyuntikkan info versi ke file EXE"""
        # Placeholder untuk pengembangan fitur metadata
        pass