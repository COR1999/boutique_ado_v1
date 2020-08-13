from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product
from django.contrib import messages
from django.db.models import Q
# Create your views here.

def all_products(request):
    """A view to show all products, including sorting and search queries"""

    products = Product.objects.all()

    if request.GET:
        if 'q' in request.GET:
            query = request.GET["q"]
            if not query:
                message.error(request, "You didnt enter any search criteria!")
                return redirect(reverse("products"))


    context = {
        "products": products,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """A view to show individual product"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context)
