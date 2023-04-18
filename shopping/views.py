from django.shortcuts import render
from .models import shopping_index, Shopping_detail
# Create your views here.

def shoppingindex(request):
    shopping_items = shopping_index.objects.all()
    return render(request, 'shopping/shopping_index.html', {'shopping_items':shopping_items})

def shopping_detail(request):
    shopping_detail = Shopping_detail.objects.all()
    return render(request, 'shopping/shopping_detail.html', {'shopping_detail': shopping_detail})