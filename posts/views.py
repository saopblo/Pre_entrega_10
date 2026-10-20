from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django import forms
from .forms import PostForm
from django.contrib.auth.decorators import login_required

def inicio(request):
    contexto_inicio = { 'titulo': 'Página de Inicio', 'seccion': 'Principal' }
    return render(request, "posts/inicio.html", contexto_inicio)

def acerca(request):
    contexto_acerca = { 'titulo': 'Acerca de', 'seccion': 'Acerca' }
    return render(request, "posts/acerca.html", contexto_acerca)

def lista_posts(request):
    posts = Post.objects.all().order_by("-fecha_creacion")

    contexto = {
        'posts':posts,
    }
    return render(request, "posts/lista_posts.html", contexto)


@login_required
def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect("inicio")
    else:
        form = PostForm()

    return render(request, "posts/post_form.html", {
                  "form": form,
                  "titulo_pagina": "Crear un post",
                  "texto_boton": "Crear",
                  })

def detalle_post(request, slug):
    post=get_object_or_404(Post, slug=slug)
    return render(request, "posts/detalle_post.html", {
                  "post": post,
                  })

@login_required
def editar_post(request, slug):
    post=get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("detalle_post", slug=post.slug)
    else:
        form = PostForm(instance=post)

    return render(request, "posts/post_form.html", {
                  "form": form,
                  "post": post, 
                  "titulo_pagina": "Editar un post",
                  "texto_boton": "Editar",
                  })


@login_required
def eliminar_post(request, slug):
    post=get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        post.delete()
        return redirect("inicio")

    return render(request, "posts/post_confirm_delete.html", {
                  "post": post,
                  })
