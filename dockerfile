# 1. IMAGEN BASE
FROM python:3.11-slim

# 2. SEGURIDAD
RUN useradd -m morgan_user
WORKDIR /home/morgan_user/app

# 3. DEPENDENCIAS DEL SISTEMA
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# === NUEVO PASO ===
# 4. LIBRERÍAS DE PYTHON: Instalamos requests de forma segura
RUN pip install --no-cache-dir requests

# 5. ARCHIVOS
COPY --chown=morgan_user:morgan_user ./app .

# 6. CAMBIO DE USUARIO
USER morgan_user

# 7. EJECUCIÓN
CMD ["python", "main.py"]