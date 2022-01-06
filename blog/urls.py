from django.urls import path
from . import views

app_name = 'blog' #for linking directly from the all_blogs page 

urlpatterns = [

    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail')
]
