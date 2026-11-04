import tkinter as tk
from tkinter import messagebox
from model.login_models import User
from views.home_view import DashboardVentana

class LoginVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("Onyx Systems // Terminal de Acceso")
        
        window_width = 380
        window_height = 420
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int((screen_width / 2) - (window_width / 2))
        center_y = int((screen_height / 2) - (window_height / 2))
        self.root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
        self.root.resizable(False, False)
        self.root.config(bg="#07080b")

        self._crear_interfaz()

    def _crear_interfaz(self):
        lbl_titulo = tk.Label(
            self.root, 
            text="ONYX SYSTEMS // LOGIN", 
            font=("Arial", 16, "bold"), 
            bg="#07080b", 
            fg="#d4af37"
        )
        lbl_titulo.pack(pady=25)

        lbl_usuario = tk.Label(
            self.root, 
            text="[ USUARIO CREDENCIAL ]", 
            font=("Consolas", 10, "bold"), 
            bg="#07080b", 
            fg="#e2e8f0"
        )
        lbl_usuario.pack(anchor="w", padx=40, pady=(5, 2))
        
        self.entry_usuario = tk.Entry(
            self.root, 
            font=("Consolas", 11), 
            bg="#12151c", 
            fg="#4193ff", 
            insertbackground="#4193ff",
            relief="solid", 
            bd=1
        )
        self.entry_usuario.pack(fill="x", padx=40, ipady=4)

        lbl_pass = tk.Label(
            self.root, 
            text="[ CONTRASEÑA ACCESO ]", 
            font=("Consolas", 10, "bold"), 
            bg="#07080b", 
            fg="#e2e8f0"
        )
        lbl_pass.pack(anchor="w", padx=40, pady=(15, 2))
        
        self.entry_pass = tk.Entry(
            self.root, 
            font=("Consolas", 11), 
            show="*", 
            bg="#12151c", 
            fg="#4193ff", 
            insertbackground="#4193ff",
            relief="solid", 
            bd=1
        )
        self.entry_pass.pack(fill="x", padx=40, ipady=4)

        btn_ingresar = tk.Button(
            self.root, 
            text="CONECTAR TERMINAL", 
            font=("Arial", 11, "bold"),
            bg="#1a2333", 
            fg="#e2e8f0", 
            activebackground="#12151c",
            activeforeground="#4193ff",
            cursor="hand2",
            relief="groove",
            bd=2,
            command=self._validar_login
        )
        btn_ingresar.pack(fill="x", padx=40, pady=35, ipady=6)

    def _validar_login(self):
        usuario_texto = self.entry_usuario.get().strip()
        pass_texto = self.entry_pass.get().strip()

        if not usuario_texto or not pass_texto:
            messagebox.showwarning("Campos Vacíos", "Por favor ingresa usuario y contraseña.")
            return

        usuario_obj = User(usuario_texto, pass_texto)
        datos_usuario = usuario_obj.auth()

        if datos_usuario and len(datos_usuario) > 0:
            usuario_encontrado = datos_usuario[0]
            nombre_usuario = usuario_encontrado.get('nombre', 'Usuario')
            
            messagebox.showinfo("Bienvenido", f"¡Hola {nombre_usuario}! Acceso concedido.")
            self._abrir_dashboard(nombre_usuario)
        else:
            messagebox.showerror("Error de Acceso", "Usuario o contraseña incorrectos.")

    def _abrir_dashboard(self, nombre_completo):
        self.root.destroy()
        root_dashboard = tk.Tk()
        DashboardVentana(root_dashboard, nombre_completo)
        root_dashboard.mainloop()
