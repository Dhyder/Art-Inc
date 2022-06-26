from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def artworks(request):
    return render(request, 'artworks.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def confirmation(request):
    return render(request, 'confirmation.html')

def gallery(request):
    return render(request, 'gallery.html')

def museum(request):
    return render(request, 'museum.html')

def shopbar(request):
    return render(request, 'shopbar.html')