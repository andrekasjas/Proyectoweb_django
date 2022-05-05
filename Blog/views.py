from django.shortcuts import render
from Blog.models import post, categorias
# Create your views here.

def blog(request):
    posts = post.objects.all()
    return render(request,'Blog/blog.html',{'posts': posts})

def categoria(request, categoria_id):
    categoris = categorias.objects.get(id = categoria_id)
    posts = post.objects.filter(categoria = categoria_id)
    return render(request, 'Blog/categorias.html', {"categoris":categoris, "posts":posts})