from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('cakes',views.cakeView)
router.register('users',views.userView)
router.register('cart',views.cartView)
router.register('orders',views.orderView)


urlpatterns = [
    path('',include(router.urls)),
    url(r'^searchcakes/(?P<cakes>[a-zA-Z]+)$',views.searchcakes.as_view()),
    path('login/', views.login.as_view()),


]

