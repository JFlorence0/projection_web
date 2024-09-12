from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'core/home.html')

def menu(request):
	return render(request, 'core/menu.html')

def membership(request):
	return render(request, 'core/membership.html')

def about_us(request):
	return render(request, 'core/about_us.html')