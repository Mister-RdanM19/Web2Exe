import customtkinter as ctk
from ui_manager import AppInterface
from compiler_core import CompilerEngine

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Builder by Mr.Rm19")
        self.geometry("600x700")

        # Hubungkan ke Mesin (Core)
        self.engine = CompilerEngine(self.update_ui_log)
        
        # Hubungkan ke Tampilan (UI)
        self.ui = AppInterface(self, self.proses_rakit)

    def update_ui_log(self, msg):
        self.ui.add_log(msg)

    def proses_rakit(self):
        nama = self.ui.name_entry.get()
        folder = self.ui.path_entry.get()
        icon = self.ui.icon_entry.get() # Ambil data icon
        
        if not nama or not folder:
            self.update_ui_log("Error: Nama dan Folder wajib diisi!")
            return

        # Masukkan ke dalam dictionary extra_configs
        configs = {
            'icon_path': icon
        }

        # Jalankan mesin dengan tambahan parameter configs
        # Gunakan threading agar GUI tidak macet saat loading lama
        import threading
        threading.Thread(target=self.engine.start_build, args=(nama, folder, configs), daemon=True).start()
        
        if not nama or not folder:
            self.update_ui_log("Error: Nama dan Folder tidak boleh kosong!")
            return

        # Jalankan mesin rarakit
        self.engine.start_build(nama, folder)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()