
from django.shortcuts import render

def instamart(request):
	# You can fetch products from the database here
	return render(request, 'instamart.html')
