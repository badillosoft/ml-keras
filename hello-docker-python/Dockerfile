# docker build -t <TAG> .
# docker image ls
# docker run -d -p <OUT-PORT>:<IN-PORT> <TAG>
# docker container ls
# docker container stop <ID>

# Indica la imagen base para nuestro contenedor
FROM python:2.7.15-slim

# Definimos la carpeta dónde será montada la aplicación
# (el sistema de archivo comienza en / para sistema unix)
WORKDIR /app

# Copiamos todos los archivos de nuestro contenedor
# a la carpeta dónde será montada la aplicación
COPY . /app

# Ejecutamos el comando pip, el cuál instalará todas las
# librerías de python contenidas en el archivo `requeriments.txt`
RUN pip install --trusted-host pypi.python.org -r requeriments.txt

# Exponemos el puerto 5000 generado por nuestra aplicación de Flask
EXPOSE 5000

# Ejecutamos el comando `python app.py`
CMD [ "python", "app.py" ]