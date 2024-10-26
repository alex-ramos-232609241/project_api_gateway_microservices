from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^users/(?P<path>.*)$', views.proxy_users),
    re_path(r'^orders/(?P<path>.*)$', views.proxy_orders),
    re_path(r'^products/(?P<path>.*)$', views.proxy_products)
]
