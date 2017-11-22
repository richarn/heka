from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'publicidad/index.html')

def hotel(request):
	return render(request, 'publicidad/hoteles.html')

def bodega(request):
	return render(request, 'publicidad/bodegas.html')

def entretenimiento(request):
	return render(request, 'publicidad/entretenimiento.html')

def santuario(request):
	return render(request, 'publicidad/santuarios.html')

def restaurante(request):
	return render(request, 'publicidad/restaurante.html')

def supermercado(request):
	return render(request, 'publicidad/supermercado.html')	