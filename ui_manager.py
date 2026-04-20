import customtkinter as ctk
from tkinter import filedialog

class AppInterface:
    def __init__(self, window, build_event):
        self.window = window
        self.build_event = build_event 
        self.setup_ui()

    def setup_ui(self):
        # Header Identitas
        # --- SWITCH PHP ENGINE ---
        self.php_switch = ctk.CTkSwitch(self.window, text="Aktifkan PHP Engine (Portable)")
        self.php_switch.pack(pady=10)
        ctk.CTkLabel(self.window, text="Builder by Mr.Rm19", 
                    font=("Arial", 24, "bold")).pack(pady=(20, 5))
        ctk.CTkLabel(self.window, text="Professional Web to EXE Creator", 
                    font=("Arial", 10)).pack(pady=(0, 20))

        # --- INPUT NAMA APLIKASI ---
        ctk.CTkLabel(self.window, text="Nama Aplikasi:").pack(anchor="w", padx=50)
        self.name_entry = ctk.CTkEntry(self.window, placeholder_text="Contoh: My_Web_App", width=500)
        self.name_entry.pack(pady=(0, 15))

        # --- INPUT FOLDER WEBSITE ---
        ctk.CTkLabel(self.window, text="Folder Website (HTML/PHP):").pack(anchor="w", padx=50)
        self.path_frame = ctk.CTkFrame(self.window, fg_color="transparent")
        self.path_frame.pack(pady=(0, 15))
        self.path_entry = ctk.CTkEntry(self.path_frame, placeholder_text="Pilih folder...", width=390)
        self.path_entry.pack(side="left", padx=(0, 10))
        ctk.CTkButton(self.path_frame, text="Cari", width=100, command=self.open_folder).pack(side="right")

        # --- INPUT ICON (Fitur Tahap 5) ---
        ctk.CTkLabel(self.window, text="Custom Icon (.ico):").pack(anchor="w", padx=50)
        self.icon_frame = ctk.CTkFrame(self.window, fg_color="transparent")
        self.icon_frame.pack(pady=(0, 15))
        self.icon_entry = ctk.CTkEntry(self.icon_frame, placeholder_text="Kosongkan untuk default", width=390)
        self.icon_entry.pack(side="left", padx=(0, 10))
        ctk.CTkButton(self.icon_frame, text="Pilih Icon", width=100, command=self.open_icon).pack(side="right")

        # --- LOG CONSOLE ---
        self.log_view = ctk.CTkTextbox(self.window, width=500, height=200, 
                                      fg_color="black", text_color="#00FF41", font=("Consolas", 11))
        self.log_view.pack(pady=10)

        # --- TOMBOL BUILD ---
        self.btn_build = ctk.CTkButton(self.window, text="RAKIT SEKARANG (EXE)", 
                                      fg_color="#1f538d", hover_color="#14375e",
                                      height=50, font=("Arial", 14, "bold"),
                                      command=self.build_event)
        self.btn_build.pack(pady=20)

    # --- FUNGSI HELPER ---
    def open_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.path_entry.delete(0, "end")
            self.path_entry.insert(0, folder)

    def open_icon(self):
        icon_file = filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])
        if icon_file:
            self.icon_entry.delete(0, "end")
            self.icon_entry.insert(0, icon_file)

    def add_log(self, text):
        self.log_view.insert("end", f"> {text}\n")
        self.log_view.see("end")