import os
import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod


class SmartDevice(ABC):
    def __init__(self, name: str):
        self._name = name

    @abstractmethod
    def execute_action(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class SmartLight(SmartDevice):
    def __init__(self):
        super().__init__("Living room smart light")

    def execute_action(self):
        return f"{self._name}: Set brightness to 100%"

    def turn_off(self):
        return f"{self._name}: Turned OFF"


class SmartSpeaker(SmartDevice):
    def __init__(self):
        super().__init__("Alexa speaker")

    def execute_action(self):
        return f"{self._name}: Set volume to 100%"

    def turn_off(self):
        return f"{self._name}: Stopped playing audio"


class SmartTV(SmartDevice):
    def __init__(self):
        super().__init__("Samsung TV")

    def execute_action(self):
        return f"{self._name}: Turn off in 30 min"

    def turn_off(self):
        return f"{self._name}: Turned OFF immediately"


class SmartAC(SmartDevice):
    def __init__(self):
        super().__init__("Air Conditioner")

    def execute_action(self):
        return f"{self._name}: Temperature set to 22°C"

    def turn_off(self):
        return f"{self._name}: Compressor powered down"


class PolymorphicAppTemplate(tk.Tk):
    def __init__(self):
        super().__init__()

        window_width = 600
        window_height = 580

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_x = int((screen_width / 2) - (window_width / 2))
        center_y = int((screen_height / 2) - (window_height / 2))

        self.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
        self.title("OOP Lab: Polymorphism GUI Template")
        self.resizable(False, False)

        dir_actual = os.path.dirname(os.path.abspath(__file__))
        icon_dir = os.path.join(dir_actual, "rabbit.ico")
        if os.path.exists(icon_dir):
            self.iconbitmap(icon_dir)

        self.cyberpunk_mode = True

        self.theme_cyber = {
            "bg_main": "#07080b",
            "bg_card": "#12151c",
            "text_head": "#d4af37",
            "text_main": "#e2e8f0",
            "text_muted": "#4193ff",
            "btn_bg": "#1a2333",
            "btn_fg": "#e2e8f0",
            "btn_off_bg": "#3a151c",
            "btn_off_fg": "#e2e8f0",
            "list_bg": "#12151c",
            "list_fg": "#e2e8f0"
        }

        self.theme_light = {
            "bg_main": "#f4f6f9",
            "bg_card": "#ffffff",
            "text_head": "#1e293b",
            "text_main": "#334155",
            "text_muted": "#2563eb",
            "btn_bg": "#1e293b",
            "btn_fg": "#ffffff",
            "btn_off_bg": "#c0392b",
            "btn_off_fg": "#ffffff",
            "list_bg": "#ffffff",
            "list_fg": "#334155"
        }

        self.items = {
            "Light": SmartLight(),
            "Speaker": SmartSpeaker(),
            "TV": SmartTV(),
            "AC": SmartAC()
        }

        self.style = ttk.Style()
        self.style.theme_use('default')

        self._build_interface()
        self._apply_theme()

    def _build_interface(self):
        top_bar = tk.Frame(self)
        top_bar.pack(fill="x", side="top", anchor="ne", padx=15, pady=10)

        self.btn_theme = tk.Button(
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

        self.lbl_star = tk.Label(
            top_bar,
            text="★",
            font=("Arial", 12)
        )
        self.lbl_star.pack(side="right", padx=(0, 6))

        self.lbl_header = tk.Label(
            self,
            text="SMART HOME POLYMORPHISM",
            font=("Arial", 18, "bold")
        )
        self.lbl_header.pack(pady=(15, 15))

        self.group_box = ttk.LabelFrame(
            self,
            text=" [ SELECT DEVICE INTERFACE ] ",
            padding=(25, 20)
        )
        self.group_box.pack(fill="x", padx=40, pady=10)

        first_key = list(self.items.keys())[0]
        self.selected_key = tk.StringVar(value=first_key)

        self.radio_buttons = []
        for key in self.items.keys():
            rb = ttk.Radiobutton(
                self.group_box,
                text=key,
                value=key,
                variable=self.selected_key
            )
            rb.pack(anchor="w", pady=6)
            self.radio_buttons.append(rb)

        frame_buttons = tk.Frame(self)
        frame_buttons.pack(pady=15)

        self.btn_action = tk.Button(
            frame_buttons,
            text="EXECUTE ACTION",
            command=self._handle_action,
            font=("Arial", 10, "bold"),
            relief="groove",
            border=2,
            cursor="hand2",
            padx=15,
            pady=8
        )
        self.btn_action.pack(side="left", padx=10)

        self.btn_turn_off = tk.Button(
            frame_buttons,
            text="TURN OFF",
            command=self._handle_turn_off,
            font=("Arial", 10, "bold"),
            relief="groove",
            border=2,
            cursor="hand2",
            padx=15,
            pady=8
        )
        self.btn_turn_off.pack(side="left", padx=10)

        self.lbl_output = tk.Label(
            self,
            text="Console idle. Awaiting hardware selection signal.",
            font=("Arial", 11, "italic"),
            relief="solid",
            bd=1,
            height=3,
            wraplength=500,
            justify="center"
        )
        self.lbl_output.pack(fill="x", padx=40, pady=5)

        self.log_frame = ttk.LabelFrame(
            self,
            text=" [ ACTIVITY LOG ] ",
            padding=(10, 5)
        )
        self.log_frame.pack(fill="both", expand=True, padx=40, pady=15)

        scrollbar = ttk.Scrollbar(self.log_frame, orient="vertical")
        self.lst_activity = tk.Listbox(
            self.log_frame,
            yscrollcommand=scrollbar.set,
            font=("Consolas", 10),
            relief="flat",
            bd=0
        )
        scrollbar.config(command=self.lst_activity.yview)

        scrollbar.pack(side="right", fill="y")
        self.lst_activity.pack(side="left", fill="both", expand=True)

    def _log_event(self, message: str):
        self.lbl_output.config(text=message, font=("Arial", 11, "italic"))
        self.lst_activity.insert(tk.END, message)
        self.lst_activity.see(tk.END)

    def _handle_action(self):
        chosen_key = self.selected_key.get()
        active_object: SmartDevice = self.items[chosen_key]
        result_message = active_object.execute_action()
        self._log_event(f"[ACTION] {result_message}")

    def _handle_turn_off(self):
        chosen_key = self.selected_key.get()
        active_object: SmartDevice = self.items[chosen_key]
        result_message = active_object.turn_off()
        self._log_event(f"[TURN OFF] {result_message}")

    def _apply_theme(self):
        t = self.theme_cyber if self.cyberpunk_mode else self.theme_light

        self.config(bg=t["bg_main"])
        self.lbl_header.config(bg=t["bg_main"], fg=t["text_head"])
        self.btn_theme.master.config(bg=t["bg_main"])
        self.lbl_star.config(bg=t["bg_main"])
        self.btn_theme.master.config(bg=t["bg_main"])
        
        for child in self.btn_theme.master.winfo_children():
            child.config(bg=t["bg_main"])

        if self.cyberpunk_mode:
            self.btn_theme.config(text="LIGHT INTERFACE", bg="#1e293b", fg="#e2e8f0")
            self.lbl_star.config(fg="#d4af37")
        else:
            self.btn_theme.config(text="NOIR INTERFACE", bg="#07080b", fg="#4193ff")
            self.lbl_star.config(fg="#2563eb")

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

        self.btn_action.config(
            bg=t["btn_bg"],
            fg=t["btn_fg"],
            activebackground=t["bg_card"],
            activeforeground=t["text_muted"]
        )
        
        self.btn_turn_off.config(
            bg=t["btn_off_bg"],
            fg=t["btn_off_fg"],
            activebackground=t["bg_card"],
            activeforeground=t["text_muted"]
        )

        self.btn_action.master.config(bg=t["bg_main"])
        self.lbl_output.config(bg=t["bg_card"], fg=t["text_muted"], highlightbackground=t["text_head"])
        self.lst_activity.config(bg=t["list_bg"], fg=t["list_fg"], selectbackground=t["text_muted"])

    def _toggle_theme(self):
        self.cyberpunk_mode = not self.cyberpunk_mode
        self._apply_theme()


if __name__ == "__main__":
    app = PolymorphicAppTemplate()
    app.mainloop()