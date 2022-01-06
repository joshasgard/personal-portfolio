from django.urls import path
from . import views

app_name = 'about' #for linking directly from the all_blogs page 

urlpatterns = [

    path('', views.about, name='about'),
]
