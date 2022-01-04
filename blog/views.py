from django.shortcuts import render

from .models import Myblogs


def all_blogs(request):
    blogposts = Myblogs.objects.all()

    return render(request, 'blog/all_blogs.html',{'myblogs':blogposts})

