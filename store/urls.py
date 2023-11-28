from django.contrib import admin
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django_daraja import mpesa, views

from .views.home import Index, store
from .views.payment import MpesaPaymentView
from .views.signup import Signup
from .views.login import Login,logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store, name='store'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', auth_middleware(Cart.as_view()), name='cart'),
    path('check-out/', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('mpesa-payment/', MpesaPaymentView.as_view(), name='payment'),
    path('api/', include('store.api.urls'))

]
