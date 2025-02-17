from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from new_app.forms import product_form
from new_app.models import product,seller

@login_required(login_url='index')
def product_upload(request):
    user_data = request.user
    seller_data = seller.objects.get(seller_data = user_data)
    if request.method == 'POST':
        form = product_form(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.product_user= seller_data
            obj.save()
            return redirect("product_details")
    else:
        form = product_form()
    return render(request, 'seller/product_upload.html', {'form': form})
@login_required(login_url='index')
def product_details(request):
    user = request.user
    seller_data = seller.objects.get(seller_data = user)
    data = product.objects.filter(product_user=seller_data)

    return render(request,"seller/view.html",{"data":data})