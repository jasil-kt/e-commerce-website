from django.urls import path

from new_app import views, admin_views, seller_views, customer_views

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
    path("seller_dashboard",views.seller_dashboard,name="seller_dashboard"),
    path("delete_customer/<int:id>/",admin_views.delete_customer,name="delete_customer"),
    path('customer_details',admin_views.customer_details,name="customer_details"),
    path('seller_details',admin_views.seller_details,name="seller_details"),
    path("update_customer/<int:id>/",admin_views.update_customer,name="update_customer"),
    path("delete_seller/<int:id>/",admin_views.delete_seller,name="delete_seller"),
    path("product_upload",seller_views.product_upload,name="product_upload"),
    path('product_details',seller_views.product_details,name="product_details"),
    path('product_view',customer_views.product_view,name="product_view"),
    path('view_product',admin_views.view_product,name="view_product"),
    path("add_cart/<int:id>/",customer_views.add_cart,name="add_cart"),
    path('cart_view',customer_views.cart_view,name="cart_view"),
    path("delete_cart/<int:id>/",customer_views.delete_cart,name="delete_cart"),
    path("buy_product/<int:id>/",customer_views.buy_product,name="buy_product"),
    path("cart_product/<int:id>/", customer_views.cart_product, name="cart_product"),
    path("order_summary",customer_views.order_summary,name="order_summary"),
    path("pay_now/<int:id>/",customer_views.pay_now,name="pay_now"),
    path("delete_product/<int:id>/",customer_views.delete_product,name="delete_product")



]