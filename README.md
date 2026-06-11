# 🤖 Morgan AI - Asistente Virtual Inteligente

Morgan AI es un asistente virtual personal desarrollado por Juan Carlos López Surian, diseñado para asistir en tareas técnicas, aprendizaje continuo, productividad y automatización.

El proyecto utiliza modelos de lenguaje ejecutados localmente mediante Ollama, permitiendo mantener la privacidad de los datos y reducir la dependencia de servicios externos.

---

# 🚀 Características Actuales

## 🧠 Inteligencia Artificial Local

Morgan utiliza:

* Ollama
* Llama 3.2 3B

Las respuestas son generadas completamente en el equipo local sin enviar información a servicios externos.

---

## 🎙️ Reconocimiento de Voz

Morgan puede escuchar instrucciones mediante el micrófono utilizando:

* OpenAI Whisper
* SoundDevice
* Scipy

Capacidades:

* Conversación por voz
* Transcripción de audio
* Reconocimiento de español

---

## 🔊 Síntesis de Voz

Morgan responde mediante voz utilizando:

* Google Text To Speech (gTTS)
* Pygame

Funciones:

* Lectura automática de respuestas
* Interacción natural por voz

---

## 💾 Memoria Conversacional

Morgan almacena las conversaciones recientes para mantener contexto durante la sesión.

Archivo:

app/data/memory.json

Capacidades:

* Historial de conversaciones
* Recuperación de contexto reciente
* Persistencia básica

---

## 🖥️ Interfaz Gráfica

La interfaz está desarrollada con:

* CustomTkinter

Características:

* Tema oscuro
* Área de conversación
* Entrada de texto
* Botón de micrófono
* Respuestas en tiempo real

---

# 🏗️ Arquitectura del Proyecto

MorganProject/

app/

├── main.py

├── core/

│ ├── brain.py

│ ├── memory.py

│ ├── voice.py

│ └── listener.py

├── ui/

│ ├── terminal.py

│ └── desktop.py

├── data/

│ └── memory.json

├── README.md

└── Dockerfile

---

# ⚙️ Tecnologías Utilizadas

## Backend

* Python 3.14
* Requests

## Inteligencia Artificial

* Ollama
* Llama 3.2 3B

## Voz

* OpenAI Whisper
* SoundDevice
* Scipy
* gTTS
* Pygame

## Interfaz

* CustomTkinter

## Utilidades

* Rich
* JSON

---

# 📦 Instalación

## 1. Clonar el repositorio

git clone <repositorio>

cd MorganProject

---

## 2. Crear entorno virtual

Windows

python -m venv morgan_env

morgan_env\Scripts\activate

---

## 3. Instalar dependencias

pip install -r requirements.txt

---

## 4. Instalar Ollama

Instalar Ollama y descargar el modelo:

ollama pull llama3.2:3b

Verificar:

ollama list

---

## 5. Ejecutar Morgan

cd app

python main.py

---

# 🔧 Dependencias Principales

requests

customtkinter

pygame-ce

gtts

rich

openai-whisper

sounddevice

scipy

---

# 🎯 Objetivos del Proyecto

Morgan busca convertirse en un asistente personal avanzado capaz de:

* Mantener conversaciones naturales
* Gestionar recordatorios
* Automatizar tareas
* Administrar agenda personal
* Controlar aplicaciones del sistema
* Integrarse con APIs externas
* Analizar documentos
* Proporcionar asistencia técnica especializada

---

# 🛣️ Hoja de Ruta

## Morgan v0.3

* Interfaz gráfica inicial
* Memoria persistente
* Reconocimiento de voz

## Morgan v0.4

* Avatar interactivo
* Indicador visual de escucha
* Indicador visual de procesamiento

## Morgan v0.5

* Apertura de aplicaciones
* Automatización básica del sistema
* Comandos personalizados

## Morgan v1.0

* Sistema de plugins
* Memoria avanzada
* Agenda inteligente
* Integración con calendarios
* Soporte para múltiples modelos IA

---

# 👨‍💻 Autor

Juan Carlos López Surian

Ingeniero Informático

Proyecto personal de investigación y desarrollo enfocado en Inteligencia Artificial, automatización y asistentes virtuales locales.
