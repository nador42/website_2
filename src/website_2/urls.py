"""
URL configuration for website_2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from blog.views import blog_post_2
from website_2.views import blog_posts, blog_post, home, signup

urlpatterns = [
    path('',home,name="home"),
    path('admin/', admin.site.urls),
    path('blog/',blog_posts,name="blog"),
    path('blog/<str:pk>/',blog_post,name="blog-post"),
    path('form/',signup,name="form"),
    path('article/',blog_post_2,name="blog-post")
]
