# Morgan - Asistente Virtual Autónomo Seguro 🤖

**Morgan** es un agente de inteligencia artificial diseñado para operar como un asistente personal interactivo. El proyecto está construido bajo una arquitectura híbrida y segura, ejecutando el núcleo de lógica en un entorno aislado de Docker y conectándose con un motor de modelado de lenguaje (LLM) local.

---

## 🏗️ Arquitectura del Sistema

El proyecto prioriza la seguridad y el aislamiento de recursos mediante la siguiente estructura:

*   **Entorno de Ejecución:** Contenedor Docker basado en `python:3.14.2`.
*   **Cerebro (LLM):** Ollama ejecutando `llama3.2:3b` nativo en el Host (Windows).
*   **Seguridad:** El contenedor corre bajo un usuario sin privilegios de administrador (`morgan_user`), mitigando riesgos de inyección de código o acceso no autorizado al sistema de archivos del Host.

---

## 🛠️ Requisitos Previos

Antes de inicializar a Morgan, asegúrate de contar con:

1.  **Docker Desktop** (con soporte para WSL2 activo).
2.  **Ollama** instalado en el sistema operativo Host.
3.  El modelo `llama3.2:3b` descargado localmente (`ollama run llama3.2:3b`).

---

## 🚀 Instalación y Despliegue

Sigue estos pasos en tu terminal para compilar y ejecutar el contenedor de Morgan:

### 1. Clonar o estructurar el proyecto
Asegúrate de tener la siguiente estructura de archivos:
```text
MorganProject/
├── Dockerfile
├── README.md
└── app/
    └── main.py