from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'publicidad/index.html')

def hotel(request):
	return render(request, 'publicidad/hoteles.html')	