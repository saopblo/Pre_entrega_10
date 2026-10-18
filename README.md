# Blog Project: CRUD Completo de Publicaciones y Archivos Media

Versión avanzada de un blog web desarrollado con **Django** y **Python**. Incorpora la gestión completa del ciclo de vida de las publicaciones (**CRUD**: Crear, Leer, Editar y Eliminar), formularios dinámicos, URLs amigables mediante `slug` y subida de imágenes de portada.

---

## 📝 Descripción y Características

El proyecto sigue el patrón **MVT** de Django y utiliza formularios basados en modelos (`ModelForm`) para procesar los datos ingresados por los usuarios:

- **Crear post (Create):** formulario dinámico que procesa el texto y la imagen de portada subida por el usuario.
- **Ver detalle (Read):** búsqueda y renderizado de cada post mediante URLs legibles impulsadas por un `SlugField`.
- **Editar post (Update):** formulario precargado con la información actual del post, utilizando el argumento `instance`.
- **Eliminar post (Delete):** borrado en dos pasos, con una pantalla intermedia de confirmación antes de eliminar el registro de la base de datos.
- **Manejo de archivos media:** almacenamiento local de imágenes subidas mediante `Pillow`, `MEDIA_ROOT` y `MEDIA_URL`.

---

## 📁 Estructura del Repositorio

```text
blog_project/
├── blog_project/              # Configuración principal (settings.py, urls.py con soporte media)
├── media/                     # Imágenes de portada cargadas por los usuarios
├── posts/                     # Aplicación principal del blog
│   ├── static/
│   │   └── posts/
│   │       └── css/
│   │           └── estilos.css        # Estilos generales
│   ├── templates/
│   │   └── posts/
│   │       ├── base.html              # Plantilla base (menú y estructura común)
│   │       ├── inicio.html            # Listado principal de publicaciones
│   │       ├── acerca.html            # Página sobre el autor
│   │       ├── crear_post.html        # Formulario para crear publicaciones
│   │       ├── detalle_post.html      # Vista individual del post por slug
│   │       ├── editar_post.html       # Formulario para editar publicaciones
│   │       └── eliminar_post.html     # Confirmación de eliminación
│   ├── admin.py               # Registro del modelo Post en el Admin
│   ├── apps.py
│   ├── forms.py               # Definición de PostForm (ModelForm)
│   ├── models.py              # Modelo Post (con ImageField y SlugField)
│   ├── urls.py                # Rutas del CRUD
│   └── views.py               # Vistas basadas en funciones (crear, detalle, editar, eliminar)
├── .gitignore                 # Excluye venv/, db.sqlite3, __pycache__/ y media/
├── manage.py                  # Script de administración de Django
├── README.md                  # Documentación del proyecto
└── requirements.txt           # Dependencias (Django, Pillow, etc.)
```

---

## ⚙️ Instalación y Puesta en Marcha

1. **Clonar el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd blog_project
   ```

2. **Crear y activar un entorno virtual:**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

3. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplicar las migraciones:**
   ```bash
   python manage.py migrate
   ```

5. **(Opcional) Crear un superusuario para el Admin:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecutar el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

   Luego abre `http://127.0.0.1:8000/` en tu navegador.

---

## 🚀 Uso

- **Inicio:** listado de todas las publicaciones.
- **Crear:** formulario para publicar un nuevo post con imagen de portada.
- **Detalle:** vista de un post accesible mediante su slug (por ejemplo, `/post/mi-primer-post/`).
- **Editar:** modifica el contenido o la imagen de un post existente.
- **Eliminar:** solicita confirmación antes de borrar el post de forma definitiva.
- **Admin:** gestión de posts desde `http://127.0.0.1:8000/admin/`.

---

## 🛠️ Tecnologías Utilizadas

- Python 3
- Django
- Pillow (procesamiento de imágenes)
- SQLite (base de datos por defecto)
- HTML5 y CSS3

---

## 📌 Notas

- Las imágenes subidas se guardan en la carpeta `media/`, que no se versiona en Git (ver `.gitignore`).
- La base de datos `db.sqlite3` tampoco se incluye en el control de versiones.

---

## 👤 Autor

Pablo Nuñez
Proyecto desarrollado como parte del curso de Python / Django: Preentrega 10.
