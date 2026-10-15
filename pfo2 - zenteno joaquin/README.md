PFO 2: Sistema de Gestión de Tareas con API y Base de Datos
1. descripcion del proyecto

el proyecto consiste en un sistema usando Python y Flask que permite registrar usuarios, verificar sus credenciales y mostrar una página de bienvenida al area de tareas.

los datos de los usuarios se almacenan en una base de datos con  SQLite y las contraseñas se guardan mediante hash.

2. Tecnologías utilizadas
SQLite
Werkzeug
Python
Flask

3. Instalación

instalar Flask mediante el siguiente comando:

pip install flask


si se utiliza el cliente en consola, instalar también:

pip install requests

4. Ejecución del servidor

Ejecutar:

python servidor


Abrir en el navegador:

http://127.0.0.1:5000/

5. Endpoints

GET /: muestra la página principal.
POST /registro: registra un usuario y almacena su contraseña hasheada.
POST /login: verifica las credenciales del usuario.
GET /tareas: muestra una página HTML de bienvenida al módulo de tareas.


6. Base de datos

Se utiliza sqLite para almacenar los usuarios de forma persistente en el archivo tareas.db.

7. Seguridad

las contraseñas se procesan con generate_password_hash() y se verifican con check_password_hash() de Werkzeug.

8. Respuestas conceptuales

¿por que hashear contraseñas?

hashear contraseñas permite evitar que se almacenen directamente en texto plano.     si alguien obtiene acceso a la base de datos, no encontrará las contraseñas originales de los usuarios. Para validar el inicio de sesión, el sistema comprueba la contraseña ingresada mediante la función de verificación del hash.

¿cuaales son las ventajas de sqlite en este proyecto?

sqlite es sencilla de utilizar, no requiere instalar ni configurar un servidor de base de datos independiente y almacena la informacionn en un archivo. Es adecuada para proyectos pequeños y educativos, y permite conservar los usuarios registrados entre ejecuciones del programa.

9. evidencias

La carpeta capturas/ contiene las capturas de pantalla de las pruebas realizadas.

10. Repositorio

En esta sección se agregará el enlace al repositorio de githhub una vez publicado el proyecto.