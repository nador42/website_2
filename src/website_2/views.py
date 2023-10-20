from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from blog.models import BlogPost
from website_2.forms import SignUpForm

def blog_posts(request):
    post=BlogPost.objects.all()

    return render(request,"blog/index.html",context={"blog_post":post})
    """blog_post=get_object_or_404(BlogPost,pk=1)
    return HttpResponse(blog_post.content)
    try:
        blog_post=BlogPost.objects.get(pk=1)
    except BlogPost.DoesNotExist:
        raise Http404("l'article n'existe pas")
    return HttpResponse(blog_post.content)
    return redirect("https://www.google.fr/")"""
def blog_post(request,pk):
    post=BlogPost.objects.get(pk=pk)
    return render(request,"blog/post.html",{"post":post})
def home(request):
    return HttpResponse("Accueil de mon site")
def signup(request):
    form=SignUpForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        return HttpResponse("Merci de vous être inscrit")
    else:

        form=SignUpForm()

    return render(request, "accounts/signup.html", {"form":form})
