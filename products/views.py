from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from cart.forms import CartAddProductForm
from .recommender import Recommender
from django.db.models import Q

# Create your views here.

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products   = Product.objects.filter(available=True)
    if category_slug:
        # language = request.LANGUAGE_CODE
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {
        'category'  :  category,
        'categories':  categories,
        'products'  :  products,
    }
    return render(request, "product/list.html", context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)

    context = {
        'product' : product,
        'cart_product_form' : cart_product_form,
        'recommended_products' : recommended_products,
    }
    return render(request, "product/detail.html", context)

def product_search(request):
    result = []
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            queryset = Q(name__icontains=query) | Q(description__icontains=query)
            result = Product.objects.filter(queryset).distinct()
            print(result)
        return render(request, 'product/search.html', {'result':result})
    return render(request, 'product/search.html')
