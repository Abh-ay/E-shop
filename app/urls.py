from . import views
from django.urls import path


urlpatterns = [


    # path('login/', views.login_view, name='login'),
    # path('home/', views.home_view, name='home'),
    # path('home/<slug:data>', views.home_view, name='home'),
    # path('logout/', views.logout_view, name='logout'),
    # path('product-detail/', views.product_detail_view, name='product-detail'),

    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('verify/<auth_token>', views.verify, name='verify'),
    path('', views.HomeView.as_view(), name='home'),
    path('home/<slug:data>', views.HomeView.as_view(), name='home'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('cart/<int:id>', views.AddToCart.as_view(), name='cart'),
    path('cart/', views.AddToCart.as_view(), name='cart'),
    path('cart/addcart/', views.AddCartItemQuantity.as_view()),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('contact-us/', views.ContactView.as_view(), name='contact-us'),
    path('page-not-found/', views.NoFoundView.as_view(), name='404'),
    path('product-detail/<int:id>',
         views.ProductView.as_view(), name='product-detail'),
    # path('cart/', views.show_cart, name='cart'),
    path('remove-cart-item/<int:id>',
         views.DeleteCartItem.as_view(), name="deleteCart"),
    path('shop/', views.shop_view, name='shop'),
    path('show_cart/', views.show_cart, name="showcart"),
    path('profile/', views.ProfileView.as_view(), name='profile')
    # path('cart/delete/<int:id>', views.delete_cart, name="deleteCart")


]
