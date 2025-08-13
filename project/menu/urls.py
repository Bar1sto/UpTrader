from django.urls import path
from . import views


urlpatterns = [
    path('', views.menu_example_view, name='home'),
    path('about/', views.about_view, name='about'),
]