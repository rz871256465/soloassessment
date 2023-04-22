from django.urls import path
from . import views

urlpatterns = [
    path('shoppingindex/', views.shoppingindex, name='shoppingindex'),
    path('shopping_detail/', views.shoppingdetail, name='shoppingdetail'),
    path('product_by_name/<str:value>/', views.product_by_name, name='product_by_name'),
    path('check_by_date/<path:date>/', views.check_by_date, name='check_by_date'),
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
]