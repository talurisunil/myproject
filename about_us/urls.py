from django.urls import path, include
from . import views

urlpatterns = [
	path('about_us/', views.about_us, name='about_us'),
	path('about_us/vision_&_mision/', views.vision_mision, name='vision_&_mision'),
	path('our_approach/', views.our_approach, name='our_approach'),
	path('our_methods/', views.our_methods, name='our_methods'),
	path('impact/', views.impact, name='impact'),
	path('recognition/', views.recognition, name='recognition'),

]