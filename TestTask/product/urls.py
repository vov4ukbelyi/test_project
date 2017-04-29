from django.conf.urls import url

from . import views

app_name = 'product'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^products/$', views.CategoriesView.as_view(), name='categories'),

]
