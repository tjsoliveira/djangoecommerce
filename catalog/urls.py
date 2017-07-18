# encoding=utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    # [\W_-]+ oermite caracteres alfanuméricos, underline e traço
    url(r'^(?P<slug>[\w_-]+)/$', views.category, name='category'),
    url(r'^produtos/(?P<slug>[\w_-]+)/$', views.product, name='product'),
]