from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('projects/', views.projects, name='projects'),
    path('projects/details/<int:id>', views.details, name='details'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]