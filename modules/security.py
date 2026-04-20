class SecurityModule:
    @staticmethod
    def get_security_configs():
        """Konfigurasi untuk mencegah user nakal"""
        return {
            "disable_dev_tools": True,
            "encryption_key": "MrRm19_Secure_Key" # Persiapan fitur enkripsi nanti
        }