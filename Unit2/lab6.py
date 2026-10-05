from tkinter import *
from tkinter import ttk
from abc import ABC, abstractmethod

# =====================================================================
# MODELO (Clases y Polimorfismo)
# =====================================================================
class SmartDevice(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def turn_on(self):
        pass

class SmartLight(SmartDevice):
    def __init__(self):
        super().__init__("Living Room Smart Light")

    def turn_on(self):
         return f"◇ {self.name} // Lumens calibrated to 100% [Status: Stable]"
        
class SmartSpeaker(SmartDevice):
    def __init__(self):
        super().__init__("Alexa Speaker")

    def turn_on(self):
         return f"◇ {self.name} // Direct link established. Routing audio: 'The Smiths'"

class SmartWatch(SmartDevice):
    def __init__(self):
        super().__init__("My Smart Watch")

    def turn_on(self):
         return f"◇ {self.name} // Internal clock synchronized at 15:00 hours"


# =====================================================================
# INTERFAZ GRÁFICA (Cyberpunk Noir / Elegante)
# =====================================================================
class SmartHomeApp(Tk):
    def __init__(self):
        super().__init__()

        # --- 1. CONFIGURACIÓN DE TAMAÑO Y CENTRADO ---
        window_width = 600
        window_height = 490

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_x = int((screen_width / 2) - (window_width / 2))
        center_y = int((screen_height / 2) - (window_height / 2))

        self.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
        self.title("Lab 6: Cyberpunk Noir Controller")
        self.resizable(False, False)

        # --- 2. CONFIGURACIÓN DE TEMAS ---
        self.cyberpunk_mode = True

        # Paleta Cyberpunk Noir (Elegante, sin rosa ni verde)
        self.theme_cyber = {
            "bg_main": "#07080b",       # Negro absoluto / Ceniza
            "bg_card": "#12151c",       # Gris grafito oscuro
            "text_head": "#d4af37",     # Ámbar / Oro viejo elegante
            "text_main": "#e2e8f0",     # Blanco cian pálido
            "text_muted": "#4193ff",    # Azul neón de medianoche / Eléctrico tenue
            "btn_bg": "#1a2333",        # Azul corporativo oscuro
            "btn_fg": "#e2e8f0"
        }

        # Paleta Luz Elegante
        self.theme_light = {
            "bg_main": "#f4f6f9",       # Blanco platino suave
            "bg_card": "#ffffff",       # Blanco puro
            "text_head": "#1e293b",     # Azul pizarra profundo
            "text_main": "#334155",     # Gris asfalto
            "text_muted": "#2563eb",    # Azul rey nítido
            "btn_bg": "#1e293b",        # Botón oscuro contrastante
            "btn_fg": "#ffffff"
        }

        # --- 3. REGISTRO DE OBJETOS ---
        self.devices = {
             "Smart Light": SmartLight(),
             "Alexa Speaker": SmartSpeaker(),
             "Smart Watch": SmartWatch(),
        }

        self.style = ttk.Style()
        self.style.theme_use('default')

        # Construir interfaz
        self._build_interface()
        self._apply_theme()

    def _build_interface(self):
        # --- CONTENEDOR SUPERIOR DERECHO ---
        top_bar = Frame(self)
        top_bar.pack(fill="x", side="top", anchor="ne", padx=15, pady=10)

        # Botón de cambio de tema
        self.btn_theme = Button(
            top_bar,
            text="SWITCH MODE",
            command=self._toggle_theme,
            font=("Arial", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=4
        )
        self.btn_theme.pack(side="right")

        # Icono de estrella al lado del botón
        self.lbl_star = Label(
            top_bar,
            text="★",
            font=("Arial", 12)
        )
        self.lbl_star.pack(side="right", padx=(0, 6))

        # --- CONTENIDO PRINCIPAL ---
        # Encabezado principal
        self.lbl_header = Label(
            self,
            text="ONYX SYSTEMS // CONSOLE",
            font=("Arial", 18, "bold")
        )
        self.lbl_header.pack(pady=(15, 15))

        # Contenedor de opciones (Radiobuttons)
        self.group_box = ttk.LabelFrame(
            self,
            text=" [ SELECT DEVICE INTERFACE ] ",
            padding=(25, 20)
        )
        self.group_box.pack(fill="x", padx=40, pady=10)

        # Selección por defecto
        first_key = list(self.devices.keys())
        self.selected_key = StringVar(value=first_key)

        self.radio_buttons = []
        for key in self.devices.keys():
            rb = ttk.Radiobutton(
                self.group_box,
                text=key,
                value=key,
                variable=self.selected_key
            )
            rb.pack(anchor="w", pady=6)
            self.radio_buttons.append(rb)

        # Botón de Acción Principal
        self.btn_action = Button(
            self,
            text="INITIALIZE PROTOCOL",
            command=self._handle_action,
            font=("Arial", 11, "bold"),
            relief="groove",
            border=2,
            cursor="hand2",
            padx=20,
            pady=10
        )
        self.btn_action.pack(pady=25)

        # Pantalla de salida / Resultados
        self.lbl_output = Label(
            self,
            text="Console idle. Awaiting hardware selection signal.",
            font=("Arial", 11, "italic"),
            relief="solid",
            bd=1,
            height=4,
            wraplength=500,
            justify="center"
        )
        self.lbl_output.pack(fill="x", padx=40, pady=5)

    def _apply_theme(self):
        """Aplica la paleta Cyberpunk Noir o Light de manera elegante."""
        t = self.theme_cyber if self.cyberpunk_mode else self.theme_light

        # Fondos de ventanas y contenedores superiores
        self.config(bg=t["bg_main"])
        self.lbl_header.config(bg=t["bg_main"], fg=t["text_head"])
        self.btn_theme.master.config(bg=t["bg_main"]) 
        self.lbl_star.config(bg=t["bg_main"])

        # Estilos adaptativos del botón de cambio de tema e icono estrella
        if self.cyberpunk_mode:
            self.btn_theme.config(text="LIGHT INTERFACE", bg="#1e293b", fg="#e2e8f0")
            self.lbl_star.config(fg="#d4af37")  # Estrella ámbar en modo oscuro
        else:
            self.btn_theme.config(text="NOIR INTERFACE", bg="#07080b", fg="#4193ff")
            self.lbl_star.config(fg="#2563eb")  # Estrella azul en modo claro

        # Configuración de componentes estructurales ttk
        self.style.configure(
            "TLabelframe", 
            background=t["bg_main"], 
            foreground=t["text_head"],
            font=("Arial", 10, "bold")
        )
        self.style.configure(
            "TLabelframe.Label", 
            background=t["bg_main"], 
            foreground=t["text_head"]
        )
        self.style.configure(
            "TRadiobutton", 
            background=t["bg_main"], 
            foreground=t["text_main"],
            font=("Arial", 11)
        )

        for rb in self.radio_buttons:
            rb.config(style="TRadiobutton")

        # Botón de acción principal
        self.btn_action.config(bg=t["btn_bg"], fg=t["btn_fg"], activebackground=t["bg_card"], activeforeground=t["text_muted"])
        
        # Caja de resultados (Mantiene el texto en cursiva por defecto)
        self.lbl_output.config(bg=t["bg_card"], fg=t["text_muted"], highlightbackground=t["text_head"])

    def _toggle_theme(self):
        """Alterna el estado del tema."""
        self.cyberpunk_mode = not self.cyberpunk_mode
        self._apply_theme()

    def _handle_action(self):
        chosen_key = self.selected_key.get()
        active_device = self.devices[chosen_key]
        result_message = active_device.turn_on()
        
        # Actualiza el texto de salida manteniendo la fuente cursiva estilizada
        self.lbl_output.config(text=result_message, font=("Arial", 11, "italic"))


# =====================================================================
# ARRANCADOR
# =====================================================================
if __name__ == "__main__":
    app = SmartHomeApp()
    app.mainloop()


#IA voy :3