from category.models import Category
from django.shortcuts import render
from product.models import Product
from django.views import View


class HomeStoreView(View):

    def get(self, request, *args, **kwargs):

        template_name = 'store/home_store.html'
        products = Product.objects.all()
        context = {
            'products': products,
        } 

        return render(request, template_name, context)
