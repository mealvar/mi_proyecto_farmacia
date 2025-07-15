-Proyecto Final – Curso de Python – Coderhouse 🐍
-Alumno: Maria Elisa Álvarez
-Comisión: #78110-python
-Profesor: Alan Exequiel Prestia


-Enlace de youtube video expplicativo: https://youtu.be/UUhNGrkoTwg (se ve como ladeado para un costado en el video, pero creo yo es por que mi pantalla es muy ancha)

Este es el proyecto final desarrollado para el curso de Python de Coderhouse. Se trata de una página web creada con Django para gestionar medicamentos, farmacéuticos y entregas, con funcionalidades de autenticación de usuarios, perfiles personalizados y un diseño simple y funcional.

🧪 Qué se puede hacer en la página
💊 Medicamentos
Agregar nuevos medicamentos

Ver la lista completa

Buscar por nombre

Editar y eliminar medicamentos

🧑‍⚕️ Farmacéuticos
Agregar farmacéuticos

Listar, editar y eliminar datos

📦 Entregas
Registrar entregas de medicamentos

Ver historial de entregas

Editar y eliminar registros

👤 Perfil de usuario y avatares
Registro e inicio de sesión de usuarios

Edición de perfil

Subida de avatar visible en la barra de navegación

📄 Página “Acerca de mí”
Contiene información personal sobre la creadora del proyecto

🧭 Cómo usar la página
Ingresar a la página y navegar por el menú superior.

Si no tenés cuenta, registrate desde el botón “Registrarse”.

Iniciá sesión para acceder a las funciones de agregar, editar y eliminar elementos.

En el perfil de usuario podés subir o cambiar tu avatar.

Usá la barra de búsqueda para encontrar medicamentos rápidamente por nombre.

🛠 Cómo correr este proyecto localmente
Clonar el repositorio:

bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
Crear un entorno virtual (opcional pero recomendado):

bash
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
Instalar las dependencias:

bash
pip install -r requirements.txt
Aplicar las migraciones:

bash
python manage.py migrate
Crear un superusuario:

bash
python manage.py createsuperuser
Ejecutar el servidor de desarrollo:

bash
python manage.py runserver
Abrir la página:

Ir a http://127.0.0.1:8000 en tu navegador
