from urllib import request
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render
from django.views import View
from .models import Cart, Product

from .forms import LoginForm, SignUpForm
from django.db.models import Q

# def login_view(request):
#     fm = LoginForm()
#     sm = SignUpForm()
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             fm = LoginForm(request=request, data=request.POST)
#             sm = SignUpForm(request.POST)
#             if fm.is_valid():
#                 uname = fm.cleaned_data['username']
#                 password = fm.cleaned_data['password']
#                 user = authenticate(username=uname, password=password)
#                 if user is not None:
#                     login(request, user)
#                     messages.success(
#                         request, 'Log in successfully!')
#                     return HttpResponseRedirect('/app/home/')
#             if sm.is_valid():
#                 print("***USER SM****")
#                 print(sm)
#                 sm.save()
#                 uname = sm.cleaned_data['username']
#                 password = sm.cleaned_data['password2']
#                 usr = authenticate(username=uname, password=password)
#                 print(usr)
#                 print(usr.is_authenticated)
#                 if usr is not None:
#                     print("****NOT NONE****")
#                     messages.success(request, "Account created successfully!")
#                     login(request, usr)
#                     return HttpResponseRedirect('/app/home/')
#         return render(request, 'login.html', {'form': fm, 'signup': sm})
#     else:
#         return HttpResponseRedirect('/app/home/', {'form': fm, 'signup': sm})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {'form': LoginForm(), 'signup': SignUpForm()})

    def post(self, request):
        if not request.user.is_authenticated:
            fm = LoginForm(request=request, data=request.POST)
            sm = SignUpForm(request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=uname, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(
                        request, 'Log in successfully!')
                    return HttpResponseRedirect('/app/home/')
            if sm.is_valid():
                print("***USER SM****")
                print(sm)
                sm.save()
                uname = sm.cleaned_data['username']
                password = sm.cleaned_data['password2']
                usr = authenticate(username=uname, password=password)
                print(usr)
                print(usr.is_authenticated)
                if usr is not None:
                    print("****NOT NONE****")
                    messages.success(request, "Account created successfully!")
                    login(request, usr)
                    return HttpResponseRedirect('/app/home/')
            return render(request, 'login.html', {'form': fm, 'signup': sm})
        else:
            return HttpResponseRedirect('/app/home/', {'form': LoginForm(), 'signup': SignUpForm()})


def checkout_view(request):
    return render(request, 'checkout.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'contact-us.html')


# def home_view(request, data=None):
    # if request.user.is_authenticated:
    #     if data == None:
    #         product = Product.objects.all()
    #     else:
    #         product = Product.objects.filter(fabric_type=data) | Product.objects.filter(
    #             product_type=data) | Product.objects.filter(color_chart=data) | Product.objects.filter(design=data)
    #     priority = product.filter(priority=True)
    #     return render(request, 'index.html', {'product': product, 'priority': priority})
    # else:
    #     return HttpResponseRedirect('/app/login/')

class HomeView(View):
    def get(self, request, data=None):
        if request.user.is_authenticated:
            if data == None:
                product = Product.objects.all()
            else:
                product = Product.objects.filter(fabric_type=data) | Product.objects.filter(
                    product_type=data) | Product.objects.filter(color_chart=data) | Product.objects.filter(design=data) | Product.objects.filter(company=data)
            priority = product.filter(priority=True)
            return render(request, 'index.html', {'product': product, 'priority': priority})
        else:
            return HttpResponseRedirect('/app/login/')


class NoFoundView(View):
    def get(self, request):
        return render(request, '404.html')


class ProductView(View):
    def get(self, request, id):
        product = Product.objects.get(pk=id)
        return render(request, 'product-details.html', {'product': product})


def cart_view(request):
    return render(request, 'cart.html')


def shop_view(request):
    return render(request, 'shop.html')


# def logout_view(request):
    # if request.user.is_authenticated:
    #     logout(request)
    #     return HttpResponseRedirect('/app/login/')


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return HttpResponseRedirect('/app/login/')


# def add_to_cart(request):
#     user = request.user
#     prod_id = request.GET.get('prod_id')
#     product = Product.objects.get(pk=prod_id)
#     cart = Cart(username=user, prod_id=product)
#     cart.save()
#     return HttpResponseRedirect('/app/cart/')

class AddToCart(View):
    def get(self, request):
        cartpass = Cart.objects.filter(user=request.user)
        amount = 0.0
        shipping_amount = 70.0
        totalamount = 0.0
        if cartpass:
            for p in cartpass:
                shipping_amount = 70
                tempamount = (p.quantity*p.product.price_range)
                amount += tempamount
                totalamount = amount+shipping_amount
            return render(request, 'cart.html', {'cart': cartpass, 'amount': amount, 'totalamount': totalamount, 'shipping_amount': shipping_amount})
        else:
            return render(request, 'empty-cart.html')

    def post(self, request, id):
        print(request.method)
        product = Product.objects.get(pk=id)
        cart = Cart(
            quantity=1, user=request.user, product=product)
        cart.save()
        if not cart == None:
            # cartpass = Cart.objects.filter(user=request.user)
            return HttpResponseRedirect('/app/cart/')
        else:
            return render(request, 'home.html')


class AddCartItemQuantity(View):
    def get(self, request):
        prod_id = request.GET['prod_id']
        print("*******PROD_ID")
        print(prod_id)
        cartpass = Cart.objects.filter(user=request.user)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0

        if cartpass:
            for p in cartpass:
                shipping_amount = 70
                tempamount = (p.quantity*p.product.price_range)
                amount += tempamount
                totalamount = amount+shipping_amount
            data = {
                'quantity': c.quantity,
                'amount': amount,
                'totalamount': totalamount
            }
            return JsonResponse(data)


def show_cart(request):
    cart = Cart.objects.filter(username=request.user)
    print("====")
    print(cart)
    return render(request, 'cart.html', {'cart_item': cart})


# def delete_cart(request, id):
#     product = Product.objects.get(pk=id)
#     cart = Cart.objects.get(prod_id=product)
#     if cart is not None:
#         cart.delete()
#         return HttpResponseRedirect('/app/cart/')
#     return render(request, 'cart.html')

class DeleteCartItem(View):
    def get(self, request, id):
        print("cart.delete====")
        print(id)
        cart = Cart.objects.get(pk=id)
        if not cart == None:
            print("cart.delete====")
            cart.delete()
            return HttpResponseRedirect('/app/cart/')

    def post(self, request, id):
        print("DeleteCartItem@@@")
        cart = Cart.objects.get(pk=id)
        if not cart == None:
            cart.delete()
            return HttpResponseRedirect('/app/cart/')
