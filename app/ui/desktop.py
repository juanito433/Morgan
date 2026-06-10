import customtkinter as ctk

from core.brain import generar_respuesta
from core.voice import hablar
from core.memory import guardar_interaccion
from core.listener import escuchar

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class MorganApp(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("Morgan AI")
        self.geometry("1000x700")

        self.crear_componentes()

    def crear_componentes(self):

        self.label_titulo = ctk.CTkLabel(
            self,
            text="Morgan AI",
            font=("Arial", 28, "bold")
        )

        self.label_titulo.pack(pady=20)

        self.chat = ctk.CTkTextbox(
            self,
            width=900,
            height=450
        )

        self.chat.pack(
            padx=20,
            pady=10
        )

        self.chat.insert(
            "end",
            "Morgan: Buenos días Señor.\n\n"
        )

        self.entry = ctk.CTkEntry(
            self,
            width=700,
            placeholder_text="Escribe un mensaje..."
        )

        self.entry.pack(
            side="left",
            padx=20,
            pady=20
        )

        self.boton_enviar = ctk.CTkButton(
            self,
            text="Enviar",
            command=self.enviar
        )

        self.boton_enviar.pack(
            side="left",
            padx=10
        )

        self.boton_microfono = ctk.CTkButton(
            self,
            text="🎤",
            width=50,
            command=self.hablar_microfono
        )

        self.boton_microfono.pack(
            side="left",
            padx=10
        )

    def enviar(self):

        pregunta = self.entry.get()

        if not pregunta:
            return

        self.chat.insert(
            "end",
            f"\nSeñor: {pregunta}\n"
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
            f"Morgan: {respuesta}\n"
        )

        hablar(
            respuesta
        )

        self.entry.delete(
            0,
            "end"
        )

    def hablar_microfono(self):

        texto = escuchar()

        if texto:

            self.entry.delete(
                0,
                "end"
            )

            self.entry.insert(
                0,
                texto
            )

            self.enviar()


def iniciar_app():

    app = MorganApp()
    app.mainloop()