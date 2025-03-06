from django.shortcuts import render
from django.templatetags.static import static


# Create your views here.
def home(request):
    return render(request,"home.html")

def products(request):
    return render(request, 'products.html')  # Ensure 'products.html' exists in the templates folder

def prod_search(request):
    return render(request, 'search_results.html')
