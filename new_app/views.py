from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

from new_app.forms import customer, seller, seller_form, customer_form, login_form


# Create your views here.
def index(request):
    return render(request,'index.html')


def dashboard(request):
    return render(request,'dashboard.html')



def login_page(request):
    form1 = login_form
    if request.method == 'POST':
        form1 = login_form(request.POST)
        if form1.is_valid():
            form1.save()
    return render(request,'loginpage.html',{"form1":form1})

def log_form(request):
    form1 =  login_form
    return render(request,"login_form.html",{"form1":form1})

def seller_login(request):
    form1 = login_form
    form2 = seller_form
    if request.method == 'POST':
        form1 = login_form(request.POST)
        form2 = seller_form(request.POST)

        if form2.is_valid() and form1.is_valid():
            seller1 =form1.save(commit=False)
            seller1.is_seller = True
            seller1.save()

            user = form1.save(commit=False)
            user. seller_data = seller1
            user.save()
            return redirect('seller_login')
    return render(request,"seller/seller_form.html",{"form1":form1,"form2":form2})

# def customer(request):
#     form1 = login_form
#     form2 = customer_form
#     return render(request,"customer.html",{"form1":form1,"form2":form2})

def customer_add(request):
    login_form1= login_form()
    customer_form1 = customer_form()

    if request.method == 'POST':
        customer_form1 = customer_form(request.POST)
        login_form1 = login_form(request.POST)

        if customer_form1.is_valid() and login_form1.is_valid():
            customer1 = login_form1.save(commit=False)
            customer1.is_customer = True
            customer1.save()

            user = customer_form1.save(commit=False)
            user.customer_data = customer1
            user.save()
            return redirect('customer_add')

    return render(request,'customer/register.html',{'customer_form':customer_form1,'login_form':login_form1 })

def admin_dashboard(request):
    return render(request,'admin/admin_dashboard.html')

def customer_dashboard(request):
    return render(request,'customer/customer_dashboard.html')

def seller_dashboard(request):
    return render(request,'seller/seller_dashboard.html')


def login_view(request):
    if request.method =='POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('admin_dashboard')
            elif user.is_customer:
                return redirect('customer_dashboard')
            elif user.is_seller:
                return redirect('seller_dashboard')
        else:
             messages.info(request,'Invalid Credentials')
    return render(request,'login_form.html',{'login_form':login_form})

