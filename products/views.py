from django.shortcuts import render
from django.http import HttpResponse
from .models import product
# Create your views here.

def get_productos(request, *args, **kwargs):
    
    products = product.objects.all()

    response =  render(request,"products/index.html", context= {"products" : products})

    # response = """<h1>Productos</h1>"""

    # for _product in products:
    #     response += "<p>{}</p>".format(_product.name)

    return HttpResponse(response)
 
