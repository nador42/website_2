from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from website_2.forms import BlogPostForm


def blog_post_2(request):
    if request.method=="POST":

        form=BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.path)

    else:
        init_value={}
        if request.user.is_authenticated:
            init_value["author"]=request.user
        init_value["date"]=datetime.today()
        form=BlogPostForm(initial=init_value)
    return render(request,"blog/post_2.html",{"form":form})
