from django.urls import path
from . import views

urlpatterns = [
    path('', views.shoppingindex, name='shoppingindex'),
    path('shopping_detail/', views.shoppingdetail, name='shoppingdetail'),
    path('product_by_name/<str:value>/', views.product_by_name, name='product_by_name'),
    path('check_by_date/<str:date>/',views.check_by_date, name='check_by_date'),
]