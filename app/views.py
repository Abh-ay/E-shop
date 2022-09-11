from django.db import IntegrityError
import uuid
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.views import View
from .models import Cart, Product, User
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password


from .forms import LoginForm, SignUpForm
from django.db.models import Q


# class LoginView(View):
#     def get(self, request):
#         return render(request, 'login.html', {'form': LoginForm(), 'signup': SignUpForm()})

#     def post(self, request):
#         print("POST REQUEST")
#         if not request.user.is_authenticated:
#             fm = LoginForm(request.POST)
#             print(fm.is_valid())
#             if fm.is_valid():
#                 username = fm.cleaned_data['email']
#                 password = fm.cleaned_data.get('password')
#                 print("CLEANED DATA")
#                 print(username)
#                 print(password)
#             else:
#                 print(request.POST)
#                 print(fm.errors)
#                 print(fm.non_field_errors)
#                 username = request.POST['username']
#                 password = request.POST['password']
#                 print("NO CLEANED DATA")
#                 print(username)
#                 print(password)
#             user = authenticate(email=username, password=password)
#             print("AUTHRNTICATE****&&")
#             print(user)
#             if user is not None:
#                 login(request, user)
#                 messages.success(
#                     request, 'Log in successfully!')
#                 return HttpResponseRedirect('/')
#             return render(request, 'login.html', {'form': fm, 'signup': SignUpForm()})
#         else:
#             return HttpResponseRedirect('/login/', {'form': LoginForm(), 'signup': SignUpForm()})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {'form': LoginForm(), 'signup': SignUpForm()})

    def post(self, request):
        print("***BEGIN*****P")
        print("IF******P")
        fm = LoginForm(data=request.POST)
        print("VALUE******P")
        print(fm.is_valid())
        print(fm)
        if fm.is_valid():
            print("***VALID ***")
            print(fm.errors)
            uname = fm.cleaned_data['username']
            pwd = fm.cleaned_data['password']
            usr = authenticate(username=uname, password=pwd)
            if usr is not None:
                print("***AUTHENTICATE***")
                login(request, usr)
                return HttpResponseRedirect('/')
        else:
            print("****INVALID*****")
            print(fm.errors)
            return render(request, 'login.html', {'form': fm, 'signup': SignUpForm()})


class RegisterView(View):
    def get(self, request):
        return render(request, 'login.html', {'form': LoginForm(), 'signup': SignUpForm()})

    def post(self, request):
        print("====&&&***===")
        sm = SignUpForm(request.POST)
        print(sm)
        print(sm.is_valid())
        try:
            if sm.is_valid():
                email = sm.cleaned_data['email']
                password = sm.cleaned_data['password1']
                pwd = make_password(password)
                auth_token = str(uuid.uuid4())
                usr = User(
                    email=email, password=pwd, auth_token=auth_token)
                if not usr is None:
                    usr.save()
                    userrr = authenticate(email=email, password=password)
                    login(request, userrr)
                    send_verify_mail(email, auth_token)
                    messages.success(
                        request, 'Account created successfully!!!')
                    return redirect('/')
            else:
                return render(request, 'login.html', {'form': LoginForm(), 'signup': sm})

        except IntegrityError as e:
            # if 'unique constraint' in e.message:
            messages.warning(request, 'Email is already taken',
                             extra_tags='signup_tags')
            return HttpResponseRedirect('/login/')


class CheckoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'checkout.html')
        else:
            redirect('/login/')


class ContactView(View):
    def get(self, request):
        return render(request, 'contact-us.html')


class HomeView(View):
    def get(self, request, data=None):
        if data == None:
            product = Product.objects.all()
        else:
            product = Product.objects.filter(fabric_type=data) | Product.objects.filter(
                product_type=data) | Product.objects.filter(color_chart=data) | Product.objects.filter(design=data) | Product.objects.filter(company=data)
        priority = product.filter(priority=True)
        return render(request, 'index.html', {'product': product, 'priority': priority})


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


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('/')


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
        if request.user.is_authenticated:
            product = Product.objects.get(pk=id)
            cart = Cart(
                quantity=1, user=request.user, product=product)
            cart.save()
            if not cart == None:
                # cartpass = Cart.objects.filter(user=request.user)
                return HttpResponseRedirect('/cart/')
            else:
                return render(request, 'home.html')
        else:
            return redirect('/login/')


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


class DeleteCartItem(View):
    def get(self, request, id):
        print("cart.delete====")
        print(id)
        cart = Cart.objects.get(pk=id)
        if not cart == None:
            print("cart.delete====")
            cart.delete()
            return HttpResponseRedirect('/cart/')

    def post(self, request, id):
        print("DeleteCartItem@@@")
        cart = Cart.objects.get(pk=id)
        if not cart == None:
            cart.delete()
            return HttpResponseRedirect('/cart/')


class ProfileView(View):
    def get(self, request):
        return render(request, 'profile.html', )
        # return render(request, 'profile.html', {'fm': CustomerForm(initial={'name': cd.name, 'locality': cd.locality, 'city': cd.city, 'district': cd.district, 'zipcode': cd.zipcode})})

    def post(self, request):
        return render(request, 'profile.html', )


def send_verify_mail(email, auth_token):
    subject = 'Your E-shopper account need to be verified'
    message = f'Hi paste the link to verify your accout http://127.0.0.1:8000/verify/{auth_token}'
    email_from = settings.EMAIL_HOST_USER
    receipent_list = [email]
    send_mail(subject, message, email_from, receipent_list)


def verify(request, auth_token):
    try:
        user_data = User.objects.filter(auth_token=auth_token).first()
        if user_data:
            if user_data.is_verified:
                messages.success(request, 'Your account is already verified')
                return redirect('/')
            user_data.is_verified = True
            user_data.save()
            messages.success(request, 'Your profile has been verified')
            return redirect('/')
        else:
            return redirect('page-not-found/')

    except Exception as e:
        print(e)
