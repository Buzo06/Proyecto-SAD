Guía para Hacer Funcionar el Código con la Base de Datos
Instalación de MySQL:

Si no tienes MySQL instalado, primero descárgalo e instálalo desde el sitio oficial de MySQL.
Asegúrate de tener un usuario con privilegios de administrador (por ejemplo, root), y si es necesario, configura una contraseña para él.
Instalación de Python y Dependencias:

Si no tienes Python instalado, descárgalo desde python.org.
Instala la librería mysql-connector-python para conectar Python con MySQL. Para ello, abre la terminal y ejecuta:
bash
Copiar código
pip install mysql-connector-python
Creación de la Base de Datos en MySQL:

Abre MySQL Workbench o el cliente de tu preferencia y conéctate al servidor.
Ejecuta el siguiente código SQL para crear la base de datos llamada proyecto:
sql
Copiar código
CREATE DATABASE proyecto;
USE proyecto;
Ejecución del Código Python:

Guarda el código Python que te proporcioné previamente en un archivo llamado gestion_bd_actualizado.py.
Asegúrate de que tu archivo de código Python esté en la misma carpeta donde deseas ejecutar el programa.
En el archivo, ajusta los parámetros de conexión si es necesario:
python
Copiar código
host="localhost",      
# Dirección del servidor MySQL 
user="root",           
# Usuario MySQL (si no es root, cámbialo)
password="",           
# Contraseña del usuario MySQL
database="proyecto"    
# Nombre de la base de datos que creaste
Ejecutar el Código:

Abre una terminal o CMD en la carpeta donde guardaste el archivo Python y ejecuta el siguiente comando:
bash
Copiar código
python gestion_bd_actualizado.py
Esto abrirá una interfaz gráfica que te permitirá interactuar con la base de datos (insertar, consultar y gestionar las sucursales).
Generar un Ejecutable (Opcional): Si deseas empaquetar el programa como un archivo ejecutable, puedes usar PyInstaller. Sigue estos pasos:

Instala PyInstaller ejecutando:
bash
Copiar código
pip install pyinstaller
En la terminal, navega a la carpeta donde está tu archivo Python y ejecuta:
bash
Copiar código
pyinstaller --onefile gestion_bd_actualizado.py
Esto generará un ejecutable en la carpeta dist llamada gestion_bd_actualizado.exe (en Windows) o gestion_bd_actualizado (en macOS/Linux).
