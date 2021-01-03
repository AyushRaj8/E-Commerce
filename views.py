from django.shortcuts import render,redirect
from django.http import HttpResponse
from ecom.models import Customer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def ShoppingStore(request):
	return render(request,"a.html")
def products(request):
	return render(request,"products.html")
def signup(request):
	return render(request,"signup.html")
def login(request):
	return render(request,"login.html")
def settings(request):
	return render(request,"settings.html")
def logout(request):
	return render(request,"logout.html")
def cart(request):
	return render(request,"cart.html")
def product(request):
	return render(request,"product.html")
@csrf_exempt
def saved(request):
	n=request.POST.get('Name')
	em=request.POST.get('E-mail')
	pas=request.POST.get('Password')
	con=request.POST.get('Contact')
	c=request.POST.get('City')
	add=request.POST.get('Address')
	obj=Customer(name=n,email=em,password=pas,contact=con,city=c,address=add)
	obj.save()
	return render(request,"products.html")
