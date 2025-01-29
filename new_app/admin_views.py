from django.shortcuts import redirect, render

from new_app.filters import SellerFilter
from new_app.forms import seller_form
from new_app.models import customer, seller, product


def customer_details(request):
    data = customer.objects.all()

    return render(request,"admin/cus_details.html",{"data":data})

def seller_details(request):
    data = seller.objects.all()
    print(data)

    return render(request,"admin/sell_details.html",{"data":data})

def delete_customer(request,id):
    data = customer.objects.get(id=id)
    data.delete()
    return redirect("seller_details")

    return render(request,"cus_details.html")


def update_customer(request,id):
    data = seller.objects.get(id=id)
    form1=seller_form(instance=data)
    if request.method == 'POST':
        data = seller_form(request.POST,instance=data)
        if data.is_valid():
            data.save()
        return redirect("seller_details")

    return render(request,"seller/seller_form.html",{"seller_form":form1})

def delete_seller(request,id):
    data = seller.objects.get(id=id)
    data.delete()
    return redirect("seller_details")

    return render(request,"sell_details.html")


def view_product(request):
    data = product.objects.all()
    seller_filter = SellerFilter(request.GET,queryset=data)
    data = seller_filter.qs

    return render(request,"admin/view_product.html",{"data":data,"seller_filter":seller_filter})