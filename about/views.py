from django.shortcuts import render
from .models import Aboutme


def about(request):
    # Show all blogs all limit the number with python list indexing
    entries = Aboutme.objects.order_by('-date')

    return render(request, 'about/aboutme.html',{'entries':entries})