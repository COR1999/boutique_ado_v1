from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm
# Create your views here.


def checkout(request):
    bag = request.session.get("bag", {})
    if not bag:
        messages.error(request, "There's nothing in your bad at the moment")
        return redirect(reverse("products"))
    
    order_form = OrderForm()
    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "striple_public_key": "pk_test_51HH4jLDjlHsBcv8nsTDlvMs1Zkdk3enUg23OOVaAJ8kliIhK4zV86NrNnNimffXD9gOrtquyNtz5DcwhxdPGBKps00vJv0uBcg"
    }
    return render(request, template, context)
