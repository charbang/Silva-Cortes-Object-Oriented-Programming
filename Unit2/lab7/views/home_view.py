import tkinter as tk

class DashboardVentana:
    def __init__(self, root, nombre_usuario):
        self.root = root
        self.root.title("Onyx Systems // Panel Principal")
        
        window_width = 450
        window_height = 280
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int((screen_width / 2) - (window_width / 2))
        center_y = int((screen_height / 2) - (window_height / 2))
        self.root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
        self.root.resizable(False, False)
        self.root.config(bg="#07080b")

        frame_main = tk.Frame(self.root, bg="#12151c", highlightbackground="#d4af37", highlightthickness=1)
        frame_main.pack(fill="both", expand=True, padx=20, pady=20)

        lbl_star = tk.Label(frame_main, text="★", font=("Arial", 14), bg="#12151c", fg="#d4af37")
        lbl_star.pack(pady=(15, 0))

        lbl_mensaje = tk.Label(
            frame_main, 
            text=f"SISTEMA INICIALIZADO\n\nUsuario Activo:\n{nombre_usuario}", 
            font=("Consolas", 12, "bold"),
            bg="#12151c",
            fg="#4193ff",
            justify="center"
        )
        lbl_mensaje.pack(expand=True, pady=10)
