from django.urls import path, include
from . import views

urlpatterns = [
	path('technology/', views.technology, name='technology'),
]