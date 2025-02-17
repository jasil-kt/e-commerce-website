from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from new_app.filters import BrandFilter
from new_app.forms import payment_form
from new_app.models import product, cart, customer, buy_now, pay

@login_required(login_url='index')
def product_view(request):
    data = product.objects.all()
    brand_filter = BrandFilter(request.GET,queryset=data)
    data = brand_filter.qs

    return render(request,"customer/product_view.html",{"data":data,"brand_filter":brand_filter})
@login_required(login_url='index')
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
@login_required(login_url='index')
def cart_view(request):
        user = request.user
        customer_data1 = customer.objects.get(customer_data = user)
        data = cart.objects.filter(customer_data=customer_data1)


        return render(request, "customer/cart_view.html", {"data": data})
@login_required(login_url='index')
def delete_cart(request,id):
    data = cart.objects.get(id=id)
    data.delete()
    return redirect("cart_view")

    return render(request,"customer/cart_view.html")

@login_required(login_url='index')
def buy_product(request,id):
    product_data = product.objects.get(id=id)
    quantity1 = product_data.quantity

    if request.method == 'POST':
      user_data = request.user
      print(user_data)

      customer_data1 = customer.objects.get(customer_data = user_data)
      print(customer_data1)
      count = request.POST.get('count')
      print(count)
      if quantity1 < int(count) :
          messages.info(request,"Insufficient stock")
          return redirect("product_view")

      obj = buy_now(customer = customer_data1, count = count,product=product_data)
      obj.save()
      return redirect("order_summary")

    return render(request, "customer/buy_now.html",{'data':product_data})
@login_required(login_url='index')
def cart_product(request,id):
    cart_data=cart.objects.get(id=id)

    print(cart_data.product_data)
    product_data = cart_data.product_data
    if request.method == 'POST':
      user_data = request.user
      print(user_data)

      customer_data1 = customer.objects.get(customer_data = user_data)
      print(customer_data1)
      count = request.POST.get('count')
      print(count)
      obj = buy_now(customer = customer_data1, count = count,product=product_data )
      obj.save()
      return redirect("order_summary")

    return render(request, "customer/buy_product_cart.html",{'data':product_data})

@login_required(login_url='index')
def order_summary(request):
    user = request.user
    customer_data1 = customer.objects.get(customer_data=user)
    data = buy_now.objects.filter(customer=customer_data1)
    for order in data:
        order.total_price = int(order.product.product_price) * order.count


    return render(request, "customer/order_summary.html", {"data": data,"customer_data":customer_data1})
@login_required(login_url='index')
def pay_now(request,id):
    order = buy_now.objects.get(id=id)
    product_quantity = order.product
    if request.method == "POST":
        form = payment_form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.buy = order
            obj.save()
            order.status = 1
            order.save()
            if product_quantity.quantity >= order.count:
                product_quantity.quantity -= order.count
                product_quantity.save()
            else:
                messages.info(request,"Insufficient stock")

            return redirect("payment_view")
    else:
        form = payment_form()

    return render(request, "customer/payment_page.html", {"form": form, "order": order})
@login_required(login_url='index')
def delete_product(request,id):
    data = buy_now.objects.get(id=id)
    data.delete()
    return redirect("order_summary")

    return render(request,"customer/order_summary.html")
@login_required(login_url='index')
def payment_view(request):
    return render(request, "customer/payment_successful.html")
@login_required(login_url='index')
def order(request):
    user = request.user
    customer_data1 = customer.objects.get(customer_data=user)
    data = pay.objects.filter(buy__customer=customer_data1)
    return render(request, "customer/my_orders.html", {"data": data})
