Proyecto Django de Filtrado de Usuarios
Este proyecto es una aplicación web desarrollada en Django que utiliza Django Rest Framework (DRF) y SQLite como base de datos. La aplicación permite filtrar usuarios en función de los parámetros especificados en la consulta y proporciona una forma rápida de crear usuarios utilizando un script en la shell de Django.

Requisitos
Asegúrate de tener instalado Python y Django en tu sistema. Puedes instalar Django utilizando pip:

bash

pip install Django
Configuración
Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local:

Clona el repositorio:

bash

git clone <URL del repositorio>
Instala las dependencias:

Navega a la carpeta del proyecto y crea un entorno virtual (opcional pero recomendado):

bash

cd nombre-del-proyecto
python -m venv venv
source venv/bin/activate  # En Windows, usa "venv\Scripts\activate"
Luego, instala las dependencias utilizando pip:

bash

pip install -r requirements.txt
Configuración de la base de datos:

Este proyecto utiliza SQLite como base de datos por defecto. No es necesario configurar una base de datos adicional. Sin embargo, si deseas utilizar otro sistema de gestión de bases de datos, puedes ajustar la configuración en settings.py.

Aplicar migraciones:

Aplica las migraciones para crear la base de datos y las tablas necesarias:

bash

python manage.py migrate
Ejecutar el servidor:

Inicia el servidor de desarrollo de Django:

bash

python manage.py runserver
La aplicación estará disponible en http://localhost:8000/.

Crear un Usuario (Script de la Shell de Django)
Para crear un usuario de forma rápida, puedes utilizar un script en la shell de Django. Sigue estos pasos:

Accede a la shell de Django:

bash

python manage.py shell
Ejecuta el script para crear un usuario

Uso
Accede a la aplicación en tu navegador o mediante un cliente de API.

Utiliza las rutas de la API para realizar consultas y filtrar usuarios según los parámetros deseados.

Puedes utilizar el script de la shell de Django para crear usuarios rápidamente cuando sea necesario.

Tecnologías Utilizadas
Django
Django Rest Framework (DRF)
SQLite
