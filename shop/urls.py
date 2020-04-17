from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('about/', views.about, name='About'),
    path('contact/', views.contact, name='ContactUs'),
    path('tracker/', views.tracker, name='Tracker'),
    path('search/', views.search, name='Search'),
    path('productView/<int:myid>', views.productView, name='ProductView'),
    path('checkout/', views.checkout, name='CheckOut'),
    path('handlerequest/', views.handlerequest, name='HandleRequest'),
]
