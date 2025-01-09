from django.urls import path

from new_app import views

urlpatterns = [
    path('',views.index,name="index"),
    path('dashboard',views.dashboard,name="dashboard"),
    # path('login',views.login,name="login"),
    path("log_form",views.log_form,name="log_form"),
    path("seller_login",views.seller_login,name="seller_login"),
    # path("customer_form", views.customer, name="customer"),
    path("customer_add", views.customer_add, name="customer_add"),
    path("login_view", views.login_view, name="login_view"),
    path("admin_dashboard",views.admin_dashboard,name="admin_dashboard"),
    path("customer_dashboard",views.customer_dashboard,name="customer_dashboard"),
    path("seller_dashboard",views.seller_dashboard,name="seller_dashboard")
]