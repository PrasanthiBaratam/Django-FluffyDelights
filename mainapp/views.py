from django.shortcuts import render,redirect
from django.templatetags.static import static
from django.template import loader
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import Product
# Create your views here.
def home(request):
    return render(request,"home.html")

def products(request):
    products = Product.objects.all()
    template = loader.get_template('products.html')
    context ={
        'prods' : products
    }
    return  HttpResponse(template.render(context, request)) # Ensure 'products.html' exists in the templates folder

def prod_search(request):
    return render(request, 'search_results.html')
# Create your views here.
def home(request):
    context = {
        'current_page' : 'home'
    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))

def product_view(request):  # This is equivalent to ListView
    products = Product.objects.all() # querying all records in the DB of entity type `Product`
    # i.e. this translates to the DQL :-> `SELECT * FROM PRODUCT;`
    # the `products` variable now contains a collection of all `Product` class objects.
    context = {
        'prods' : products, # the key `prods` will now be available to use in the django template design 
        'current_page' : 'products'

    } # context dictionary for passing data for rendering 
    template = loader.get_template('products.html') # creating a template object from the designed template html
    return HttpResponse(template.render(context, request)) # creates a response object after rendering
    # the returned response has the html of completed webpage including required data.

# view function for rendering individual product page 
def product_details(request, id): # This is equivalent to DetailView
    product = Product.objects.get(id = id) # select * from products where id = <parameter_id>
    context = {
        'prod' : product,
        'current_page' : 'products'
    }
    template = loader.get_template('prod_details.html')
    return HttpResponse(template.render(context, request))


    # CRUD 
# 1. C - Create
class AddProduct(CreateView):
    model = Product # specifying the schema to insert record into
    fields = [ # specifying the fields to be generated in the form
        'name',
        'price',
        'description',
        'stock',
        'pic'
    ]
    template_name = 'addProduct.html'
    success_url = reverse_lazy('prod_page') # redirect to products page after adding product


# 2. R - Read

class ProductsView(ListView):
    model = Product
    template_name = 'productsView.html'
    ordering = ['-id'] # to sort in descending order

## Search results

def searchView(request):
    query = request.GET.get('search_text') 
    # fetch the query text from GET request 
    
    results = Product.objects.filter(name__icontains = query) 
    # collect the product objects matching the name
    
    context = {
        'items' : results,
        'query' : query
    }
    template = loader.get_template('searchResults.html')
    return HttpResponse(template.render(context, request))

# 3. U - Update

class EditProduct(UpdateView):
    model = Product
    template_name = 'editProduct.html'
    fields = '__all__'
    success_url = reverse_lazy('prod_page')

# 4. D - Delete

class DelProduct(DeleteView):
    model = Product
    template_name = 'delProduct.html'
    success_url = reverse_lazy('homepage')
    
