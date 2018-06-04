from django.shortcuts import render

# Create your views here.
def technology(request):
	return render(request, 'technology/technology.html')
