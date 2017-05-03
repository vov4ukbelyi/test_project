from django.conf.urls import url

from . import views

app_name = 'product'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^products/$', views.CategoriesView.as_view(), name='categories'),
    url(r'^products/products24h/$', views.Products24hView.as_view(), name='products24h'),
    url(r'^products/(?P<category_slug>[\w-]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^products/(?P<category_slug>[\w-]+)/(?P<product_slug>[\w-]+)/$', views.AboutView.as_view(), name='about'),

]
