from django.shortcuts import render
# Create your views here.

def about_us(request):
	return render(request, 'about_us/about_us.html')

def vision_mision(request):
	return render(request, 'about_us/vision_&_mision.html')

def our_approach(request):
	return render(request, 'service/our_approach.html')

def our_methods(request):
	return render(request, 'service/our_methods.html')

def impact(request):
	return render(request, 'service/impact.html')

def recognition(request):
	return render(request, 'service/recognition.html')
