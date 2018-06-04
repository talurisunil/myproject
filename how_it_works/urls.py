from django.urls import path, include
from . import views

urlpatterns = [
	path('how_it_works/', views.how_it_works, name='how_it_works'),
]