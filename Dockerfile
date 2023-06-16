# Usa una imagen base con Python preinstalado
FROM python:3.10.4-alpine3.15

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY ./requirements.txt ./

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido del directorio actual al contenedor
COPY ./ ./

# Define los comandos por defecto cuando se ejecuta el contenedor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
