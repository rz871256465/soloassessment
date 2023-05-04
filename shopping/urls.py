from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shoppingindex/', views.shoppingindex, name='shoppingindex'),
    path('shopping_detail/', views.shoppingdetail, name='shoppingdetail'),
    path('product_by_name/<str:value>/', views.product_by_name, name='product_by_name'),
    path('check_by_date/<path:date>/', views.check_by_date, name='check_by_date'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view,name='login'),
    path('logout/', views.logout_view,name='logout'),
    path('cart/',views.add_to_cart, name='cart'),
    path('remove_from_cart/', views.remove_from_cart, name='remove_from_cart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('error/', views.error, name='error'),
]