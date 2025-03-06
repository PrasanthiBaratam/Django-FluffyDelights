from django.shortcuts import render

def login_view(request):
    return render(request, 'authentication/login.html')  # Ensure this template exists
def register_view(request):
    return render(request,'authentication/registration.html')