from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('blogpost/<int:id>', views.blogpost, name='BlogPost'),
]
