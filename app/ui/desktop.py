import customtkinter as ctk
import threading

from core.brain import generar_respuesta
from core.voice import hablar
from core.listener import escuchar
from core.memory import guardar_interaccion

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class MorganApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Morgan")
        self.geometry("1200x700")

        self.crear_interfaz()

    def crear_interfaz(self):

        self.titulo = ctk.CTkLabel(
            self,
            text="MORGAN",
            font=("Segoe UI", 30, "bold")
        )

        self.titulo.pack(pady=20)

        self.chat = ctk.CTkTextbox(
            self,
            width=1100,
            height=500,
            font=("Consolas", 15)
        )

        self.chat.pack(padx=20, pady=10)

        self.chat.insert(
            "end",
            "Morgan: Buenos días Señor. Estoy lista para ayudar.\n\n"
        )

        self.frame_input = ctk.CTkFrame(self)
        self.frame_input.pack(fill="x", padx=20, pady=10)

        self.entry = ctk.CTkEntry(
            self.frame_input,
            placeholder_text="Escriba un mensaje...",
            width=850
        )

        self.entry.pack(
            side="left",
            padx=10,
            pady=10
        )

        self.btn_enviar = ctk.CTkButton(
            self.frame_input,
            text="Enviar",
            command=self.enviar
        )

        self.btn_enviar.pack(
            side="left",
            padx=10
        )

        self.btn_microfono = ctk.CTkButton(
            self.frame_input,
            text="🎤",
            width=50,
            command=self.activar_microfono
        )

        self.btn_microfono.pack(
            side="left",
            padx=10
        )

    def enviar(self):

        pregunta = self.entry.get()

        if not pregunta:
            return

        self.chat.insert(
            "end",
            f"Señor: {pregunta}\n"
        )

        self.entry.delete(0, "end")

        threading.Thread(
            target=self.procesar_respuesta,
            args=(pregunta,),
            daemon=True
        ).start()

    def procesar_respuesta(self, pregunta):

        self.chat.insert(
            "end",
            "Morgan está pensando...\n"
        )

        respuesta = generar_respuesta(
            pregunta
        )

        guardar_interaccion(
            pregunta,
            respuesta
        )

        self.chat.insert(
            "end",
            f"Morgan: {respuesta}\n\n"
        )

        hablar(
            respuesta
        )

    def activar_microfono(self):

        threading.Thread(
            target=self.procesar_microfono,
            daemon=True
        ).start()

    def procesar_microfono(self):

        self.chat.insert(
            "end",
            "🎤 Escuchando...\n"
        )

        texto = escuchar()

        if texto:

            self.chat.insert(
                "end",
                f"Señor (voz): {texto}\n"
            )

            self.procesar_respuesta(
                texto
            )


def iniciar_app():

    app = MorganApp()
    app.mainloop()