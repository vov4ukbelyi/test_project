from django.views import generic
from .models import Category, Product

class IndexView(generic.ListView):
    template_name = 'product/index.html'

    def get_queryset(self):
        pass

class CategoriesView(generic.ListView):
    template_name = 'product/categories.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        return Category.objects.all()

class DetailView(generic.DetailView):
    model = Category
    template_name = 'product/detail.html'
    slug_url_kwarg = 'category_slug'

class AboutView(generic.DetailView):
    model = Product
    template_name = 'product/about.html'
    slug_url_kwarg = 'product_slug'