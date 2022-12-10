from django.shortcuts import render

from django.http import HttpResponse

# PRODUCT VIEWS

#http://127.0.0.1:8000/products/index
def index(request):
    return HttpResponse("products index.")

