from django.contrib import messages
from django.shortcuts import render, redirect

from new_app.filters import BrandFilter
from new_app.models import product, cart, customer


def product_view(request):
    data = product.objects.all()
    brand_filter = BrandFilter(request.GET,queryset=data)
    data = brand_filter.qs

    return render(request,"customer/product_view.html",{"data":data,"brand_filter":brand_filter})

def add_cart(request,id):
    user_data = request.user
    product_data = product.objects.get(id=id)
    customer_data1 = customer.objects.get(customer_data=user_data)
    addcart = cart.objects.filter(product_data=product_data,customer_data=customer_data1)
    if addcart.exists():
        messages.info(request,'Already added to cart')
        return redirect("product_view")
    else:
       obj = cart()
       obj.product_data = product_data
       obj.customer_data = customer_data1
       obj.save()
       messages.info(request,"Product Added to Cart")
       return redirect("product_view")


    return render(request, "customer/product_view.html",{"user_data":user_data})

def cart_view(request):
        user = request.user
        customer_data1 = customer.objects.get(customer_data = user)
        data = cart.objects.filter(customer_data=customer_data1)


        return render(request, "customer/cart_view.html", {"data": data})

def delete_cart(request,id):
    data = cart.objects.get(id=id)
    data.delete()
    return redirect("cart_view")

    return render(request,"customer/cart_view.html")

def buy_now(request,id):
    data = cart.objects.get(id=id)
    return render(request, "customer/buy_now.html",{'data':data})