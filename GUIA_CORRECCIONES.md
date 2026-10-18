# Guía de las correcciones hechas en `blog_django`

> Pensado para principiantes en Python/Django. Cada corrección explica **qué estaba mal**, **por qué rompía** y **cómo se arregló**.

---

## 1. `posts/forms.py` — faltaban los imports (bloqueaba el servidor)

**Qué estaba mal:** el archivo empezaba directo con `class PostForm(forms.ModelForm)` pero nunca importaba `forms` ni `Post`. Django fallaba al arrancar con `NameError: name 'forms' is not defined`.

**Cómo se arregló:** agregar al inicio:
```python
from django import forms
from .models import Post
```
El `.` en `from .models` significa "del mismo paquete (la app `posts`)", es la forma correcta de importar dentro de una app Django.

---

## 2. Migración faltante del campo `slug` (rompía `/posts/`)

**Qué estaba mal:** el modelo `Post` tenía un campo `slug`, pero en la base de datos SQLite esa columna **no existía**, porque nunca se corrió `makemigrations`. Al listar posts, Django intentaba leer `posts_post.slug` y SQLite lanzaba `no such column: posts_post.slug`.

**Cómo se arregló:**
```bash
python manage.py makemigrations posts   # genera 0004_post_slug.py
python manage.py migrate posts          # aplica la migración a la BD
```
**Concepto clave:** en Django, cada vez que cambiás un modelo, tenés que crear una migración (`makemigrations`) y aplicarla (`migrate`). El código Python y la base de datos son dos cosas distintas.

Después rellené a mano los slugs de los 3 posts que ya existían (quedaron en `NULL` porque se crearon antes de tener slug). Si no, sus enlaces (`detalle_post`, `editar_post`, `eliminar_post`) no funcionarían.

---

## 3. `post_form.html` — error de sintaxis del template

**Qué estaba mal:** la primera línea decía `{extends "posts/base.html" %}` en vez de `{% extends "posts/base.html" %}`. Faltaba el `%` inicial. Django tiraba `TemplateSyntaxError` al abrir crear/editar post.

**Cómo se arregló:** corregir la línea a `{% extends "posts/base.html" %}` y envolver el contenido en `{% block content %}...{% endblock %}` para que herede correctamente del layout base.

El `enctype="multipart/form-data"` ya estaba en el `<form>`, que es **obligatorio** para que el navegador envíe archivos (las imágenes). Sin eso, el campo `imagen` llega vacío siempre.

---

## 4. Templates `crear_post.html` y `editar_post.html` no existían

**Qué estaba mal:** las vistas `crear_post` y `editar_post` pedían renderizar `posts/crear_post.html` y `posts/editar_post.html`, pero esos archivos no existían. Django tiraba `TemplateDoesNotExist`.

**Cómo se arregló:** en `views.py` cambié ambas vistas para que usen el template único `posts/post_form.html` que ya existía (es el patrón correcto: un mismo formulario para crear y editar). La vista pasa `post` solo en edición, y el template usa `{% if post and post.imagen %}` para mostrar la imagen actual solo cuando corresponde.

---

## 5. `lista_posts.html` y `detalle_post.html` — contenido fuera del bloque

**Qué estaba mal:** ambos templates tenían el HTML suelto, fuera de `{% block content %}`. Al extender `base.html`, Django descarta todo lo que no está dentro de un bloque, así que la página salía **en blanco** (solo header/footer del base).

**Cómo se arregló:** envolver todo el contenido en `{% block content %}...{% endblock %}`. También se agregó `{% block title %}` para que el título de la pestaña del navegador sea correcto.

---

## 6. `eliminar_post` (views.py) — lógica muerta

**Qué estaba mal:** la vista tenía el `render` de confirmación **dentro** del `if request.method == "POST"`, después de un `return redirect(...)`. Ese código era inalcanzable: en GET la función devolvía `None` y Django tiraba error. Además pedía `eliminar_post.html`, que no existía.

**Cómo se arregló:** mover el `render` fuera del `if`, para que en GET muestre la confirmación y en POST borre y redirija. Y apuntar al template `post_confirm_delete.html`.

---

## 7. `post_confirm_delete.html` — estaba vacío

**Qué estaba mal:** el archivo existía pero tenía 0 bytes. Al abrir "Eliminar" no se veía nada.

**Cómo se arregló:** escribir un template con la confirmación ("¿Seguro que querés eliminar...?"), un `<form method="post">` con `{% csrf_token %}` y un botón "Sí, eliminar", más un enlace "Cancelar" que vuelve al detalle.

---

## 8. `base.html` — nav sin enlace al listado

**Qué estaba mal:** el menú solo tenía "Inicio" y "Acerca de", no había forma de llegar a los posts desde la navegación.

**Cómo se arregló:** agregar `<a href="{% url 'lista_posts' %}">Posts</a>` en el `<nav>`.

---

## 9. `AGENTS.md` creado en la raíz

Archivo de contexto para OpenCode: describe el proyecto, tecnologías, comandos clave, estructura, convenciones, estado actual y los pendientes. Así, en chats nuevos, OpenCode recupera el contexto sin empezar de cero.

---

## Resumen de comandos que quedaron funcionando

```bash
python manage.py check          # sin issues
python manage.py runserver      # http://127.0.0.1:8000/
```

Rutas verificadas (todas responden 200): `/`, `/posts/`, `/acerca/`, `/posts/crear/`.

---

## Pendientes (no se tocaron, quedan para después)

- `settings.py` usa `MAILERS` (no es clave válida de Django; lo estándar es `EMAIL_BACKEND`).
- `requirements.txt` mezcla dependencias del blog con las del entorno del editor (`opencode-ai`, `httpx`, `pydantic`). Conviene depurarlo.
- `Post.save()` genera el slug con `slugify(titulo)` pero si dos posts tienen el mismo título, el slug se repite y viola el `unique=True`. Conviene manejar colisiones (agregar un sufijo numérico).
- El modelo `Post` no tiene `__str__`? Sí lo tiene. Pero no hay tests; `posts/tests.py` está vacío.
- No hay `LOGIN` ni control de usuarios: cualquier visitante puede crear/editar/eliminar posts. Para un blog real, convendría agregar autenticación.

---

## Conceptos que conviene recordar (principiante)

1. **MVT**: Django es Model (datos) + View (lógica) + Template (HTML). La URL decide qué view se ejecuta.
2. **Migraciones**: el código Python define el modelo, pero la BD real se actualiza con `makemigrations` + `migrate`. Son pasos manuales.
3. **Template inheritance**: `{% extends "base.html" %}` + `{% block content %}`. Lo que no esté dentro de un bloque se descarta.
4. **CSRF**: todo `<form method="post">` necesita `{% csrf_token %}` o Django rechaza el envío.
5. **Archivos subidos**: para que el formulario envíe imágenes, el `<form>` necesita `enctype="multipart/form-data"`, y la view debe pasar `request.FILES` al form.
6. **Imports relativos**: `from .models import Post` (con punto) es la forma correcta dentro de una app. `from models import Post` (sin punto) falla.
