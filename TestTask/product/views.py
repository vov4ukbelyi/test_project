from django.views import generic
from .models import Category

class IndexView(generic.ListView):
    template_name = 'product/index.html'

    def get_queryset(self):
        pass

class CategoriesView(generic.ListView):
    template_name = 'product/categories.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        return Category.objects.all()