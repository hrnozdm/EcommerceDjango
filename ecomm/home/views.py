from django.shortcuts import render
from products.models import Product

def index(request):
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(product_name__icontains=query)
    else:
        products = Product.objects.all()
    context = {'products': products, 'query': query}
    return render(request, 'home/index.html', context)
