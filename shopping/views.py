from django.shortcuts import render, redirect
from .models import shopping_index, Shopping_detail, cart
from django.http import Http404
import plotly.graph_objs as go
from plotly.offline import plot
from django.db.models import Q
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.
def index(request):
    try:
        return render(request, 'shopping/index.html')
    except:
        raise Http404("Index not found")
@login_required
def shoppingindex(request):
    try:
        query = request.GET.get('query', '')
        price_min = request.GET.get('price_min', '')
        price_max = request.GET.get('price_max', '')
        initial_letter = request.GET.get('initial_letter', '')

        shopping_items = shopping_index.objects.filter(
            Q(product_name__icontains=query) |
            Q(manufacturer__icontains=query) |
            Q(country__icontains=query)
        )

        if price_min:
            shopping_items = shopping_items.filter(price__gte=price_min)
        if price_max:
            shopping_items = shopping_items.filter(price__lte=price_max)

            # Add initial letter filter
        if initial_letter:
            shopping_items = shopping_items.filter(product_name__istartswith=initial_letter)

        paginator = Paginator(shopping_items, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj': page_obj,
            'query': query,
            'price_min': price_min,
            'price_max': price_max,
            'initial_letter': initial_letter,
        }

        return render(request, 'shopping/shopping_index.html', context)
    except:
        raise Http404("Shopping index not found")
def shoppingdetail(request):
    try:
        shopping_details = Shopping_detail.objects.all()
        return render(request, 'shopping/shopping_detail.html', {'shopping_details': shopping_details})
    except:
        raise Http404("Shopping detail not found")

@user_passes_test(lambda u: u.is_superuser, login_url='/admin/login/')
@staff_member_required
def product_by_name(request, value):
    try:
        produce_noorder = Shopping_detail.objects.filter(product_name=value)
        produces = produce_noorder.order_by('date')
        produce = produces.first()
        if produce.latitude.endswith('N'):
            produces_lat = float(produce.latitude[:-1])
        else:
            produces_lat = -float(produce.latitude[:-1])
        if produce.longitude.endswith('E'):
            produces_lng = float(produce.longitude[:-1])
        else:
            produces_lng = -float(produce.longitude[:-1])

        x_data = [produce.date for produce in produces]
        y_data = [float(produce.price) for produce in produces]
        trace = go.Scatter(x=x_data, y=y_data, mode='markers')
        data = [trace]
        layout = go.Layout(title='Price Trends ' + value, xaxis=dict(title='Date'), yaxis=dict(title='price'))
        fig = go.Figure(data=data, layout=layout)
        div = fig.to_html(full_html=False)
        context = {
            'produces': produces,
            'produces_lat': produces_lat,
            'produces_lng': produces_lng,
            'plot_div': div,
            'produce_noorder': produce_noorder,
        }
        return render(request, 'shopping/product_by_name.html', context)
    except:
        raise Http404("Product not found")

def check_by_date(request, date):
    try:
        datesnoorder = Shopping_detail.objects.filter(date=date)
        dates = datesnoorder.order_by('price')
        x_data = [product.uniq_id for product in dates]
        y_data = [float(date.price) for date in dates]
        trace = go.Scatter(x=x_data, y=y_data, mode='markers')
        data = [trace]
        layout = go.Layout(title='Shopping Detail on ' + str(date), xaxis=dict(title='uniq_id'), yaxis=dict(title='price'))
        fig = go.Figure(data=data, layout=layout)
        div = fig.to_html(full_html=False)
        context = {
            'dates': dates,
            'plot_div': div,
        }
        return render(request, 'shopping/check_by_date.html', context)
    except Exception as e:
        # Handle any exception that might occur
        return render(request, 'shopping/error.html', {'error': str(e)})

def register_view(request):
    if request.method == 'POST':
        # 检查请求方法是否为 POST

        form = UserCreationForm(request.POST)
        # 根据 UserCreationForm 创建表单实例，并传入 POST 数据

        if form.is_valid():
            # 检查表单数据是否有效
            user = form.save()
            # 保存用户信息

            # 注册成功后可以执行其他操作，例如自动登录等

            return redirect('/')
            # 返回注册成功后的页面，这里假设 home 是一个 URL 名称
    else:
        form = UserCreationForm()
        # 若请求方法不是 POST，则创建一个空的 UserCreationForm 实例

    return render(request, 'registration/register.html', {'form': form})
    # 渲染注册页面并传递表单实例给模板

def login_view(request):
    if request.method == 'POST':
        # 处理登录表单的提交
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 验证表单数据
            user = form.get_user()
            login(request, user)
            messages.success(request, '登录成功')
            return redirect('/')  # 重定向到 index 页面
        else:
            # 登录失败
            messages.error(request, '登录失败，请检查用户名和密码')
    else:
        # 渲染登录页面
        form = AuthenticationForm(request)
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER', reverse('index')))


def add_to_cart(request):
    try:
        if request.method == 'POST':
            product_name = request.POST['product_name']
            price = float(request.POST['price'])
            quantity = int(request.POST.get('quantity', 1))
            cart_item, created = cart.objects.get_or_create(
                product_name=product_name,
                price=price,
                defaults={'quantity': quantity },
            )
            if not created:
                cart_item.quantity = quantity
                cart_item.save()
            cart_list = cart.objects.all()
            total = sum([item.price * item.quantity for item in cart_list])
            return render(request, 'shopping/cart.html', {'cart_list': cart_list, 'new_product': {'product_name': product_name, 'price': price}, 'total': total})
        else:
            cart_list = cart.objects.all()
            total = sum([item.price * item.quantity for item in cart_list])
            return render(request, 'shopping/cart.html', {'cart_list': cart_list, 'total': total})
    except Exception as e:
        # Handle any exception that might occur
        return render(request, 'shopping/error.html', {'error': str(e)})

def remove_from_cart(request):
    try:
        if request.method == 'POST':
            product_name = request.POST['product_name']
            price = float(request.POST['price'])
            cart_item = cart.objects.get(product_name=product_name, price=price)
            cart_item.delete()
        cart_list = cart.objects.all()
        total = sum([item.price * item.quantity for item in cart_list])
        return render(request, 'shopping/cart.html', {'cart_list': cart_list, 'total': total})
    except Exception as e:
        # Handle any exception that might occur
        return render(request, 'shopping/error.html', {'error': str(e)})


def error(request, exception):
    return render(request, 'error.html', {'exception': exception})



