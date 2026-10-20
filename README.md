# Blog Project: Python y Django (Preentrega 11)


Aplicación web de blog desarrollada con **Python** y **Django**. Incluye el ciclo de vida completo de las publicaciones (**CRUD**), URLs amigables mediante `slug`, subida de imágenes de portada y un **sistema de autenticación de usuarios y perfiles** (login, logout, registro y avatares).

---

## 📝 Características Principales

### 🔐 Autenticación y cuentas (`accounts`)
- **Registro** de nuevos usuarios con `UserCreationForm`.
- **Inicio y cierre de sesión** mediante las vistas de autenticación.
- **Perfil de usuario:** edición de datos y carga de avatar/foto de perfil, vinculada al modelo `User` mediante un `OneToOneField`.

### 📰 Gestión de publicaciones (`posts`)
- **Crear (Create):** formulario dinámico (`ModelForm`) con carga de imagen de portada.
- **Leer (Read):** listado principal y vista de detalle accesible por `SlugField`.
- **Editar (Update):** modificación de posts existentes, con el formulario precargado mediante `instance`.
- **Eliminar (Delete):** borrado seguro con pantalla de confirmación previa.

### 🛡️ Seguridad y permisos
- Vistas críticas protegidas con el decorador `@login_required`.
- Asignación automática del usuario autenticado como autor del post (`post.autor = request.user`).

### 🖼️ Archivos media e imágenes
- Almacenamiento local de portadas y avatares con `Pillow`, `MEDIA_ROOT` y `MEDIA_URL`.

---

## 📁 Estructura del Repositorio

```text
blog_project/
├── blog_project/              # Configuración principal (settings.py, urls.py)
├── media/                     # Archivos e imágenes subidos (portadas, avatares)
├── posts/                     # App de publicaciones (CRUD)
│   ├── static/
│   │   └── posts/css/estilos.css
│   ├── templates/posts/
│   │   ├── base.html          # Plantilla base (menú y estructura común)
│   │   ├── inicio.html        # Listado principal de publicaciones
│   │   ├── crear_post.html    # Formulario para crear publicaciones
│   │   ├── detalle_post.html  # Vista individual del post por slug
│   │   ├── editar_post.html   # Formulario para editar publicaciones
│   │   └── eliminar_post.html # Confirmación de eliminación
│   ├── admin.py
│   ├── forms.py               # PostForm (ModelForm)
│   ├── models.py              # Modelo Post (ImageField y SlugField)
│   ├── urls.py                # Rutas del CRUD
│   └── views.py               # Vistas de crear, detalle, editar y eliminar
├── accounts/                  # App de autenticación y usuarios
│   ├── templates/accounts/
│   │   ├── login.html         # Inicio de sesión
│   │   ├── registro.html      # Registro de usuarios
│   │   ├── perfil.html        # Perfil del usuario
│   │   └── agregar_avatar.html# Carga de foto de perfil
│   ├── admin.py
│   ├── forms.py
│   ├── models.py              # Modelo Avatar (OneToOneField con User)
│   ├── urls.py
│   └── views.py
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
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crear un superusuario (opcional, para el Admin):**
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

| Sección    | Descripción                                                        |
|------------|--------------------------------------------------------------------|
| Inicio     | Listado de todas las publicaciones                                 |
| Registro   | Creación de una cuenta de usuario                                  |
| Login      | Inicio de sesión (requerido para crear, editar o eliminar posts)   |
| Perfil     | Edición de datos y carga de avatar                                 |
| Crear      | Publicación de un nuevo post con imagen de portada                 |
| Detalle    | Vista de un post mediante su slug (ej: `/post/mi-primer-post/`)    |
| Editar     | Modificación del contenido o la imagen de un post propio           |
| Eliminar   | Confirmación previa al borrado definitivo del post                 |
| Admin      | Gestión de posts y usuarios en `http://127.0.0.1:8000/admin/`     |

---

## 🛠️ Tecnologías Utilizadas

- Python 3
- Django
- Pillow (procesamiento de imágenes)
- SQLite (base de datos por defecto)
- HTML5 y CSS3

---

## 📌 Notas

- Los archivos subidos se guardan en `media/`, carpeta excluida del control de versiones (ver `.gitignore`).
- `db.sqlite3` tampoco se versiona.
- Solo los usuarios autenticados pueden crear, editar o eliminar publicaciones.

---

## 👤 Autor

Pablo Nuñez
Proyecto desarrollado como parte del curso de Python / Django: Preentrega 11.
