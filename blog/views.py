from django.shortcuts import render, get_object_or_404

from .models import Myblogs


def all_blogs(request):
    # Show all blogs all limit the number with python list indexing
    blogposts = Myblogs.objects.order_by('-date')[:3]

    return render(request, 'blog/all_blogs.html',{'myblogs':blogposts})

def detail(request, blog_id):
    blog = get_object_or_404(Myblogs, pk=blog_id)
    return render(request, 'blog/details.html',{'blog':blog})