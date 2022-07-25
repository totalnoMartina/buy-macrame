from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product

def index(request):
    """ A view to return homepage """
    return render(request, 'mainapp/index.html')

@login_required
def product_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'unicorn/shopmacrames.html', context)