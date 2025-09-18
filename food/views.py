
from django.shortcuts import render

def food(request):
    # You can fetch products from the database here
    return render(request, 'food.html')
