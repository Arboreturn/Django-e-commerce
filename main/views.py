from django.shortcuts import render,get_list_or_404,get_object_or_404
from main.models import Item,Category
from django.db.models import Count
from django.views import View
# Create your views here.
def index(request):
    context = dict()
    context['items'] = Item.objects.all()[0:8]
    print(request.session.session_key)
    return render(request,'index.html',context)

def contact(request):
    context = dict()
    return render(request,'contact.html',context)


def detail(request,pk,category_slug):
    
    item = Item.objects.get(pk=pk)
    category = Category.objects.filter()
    context = {
        'items':item,
        'categories':category
    }
    return render(request,'product-detail.html',context) 
    


def category_show(request, category_slug):
    context = dict()
    context['category'] =Category.objects.all()

    context['show'] = Item.objects.filter(
        category__slug=category_slug,
    )

    return render(request, 'product.html', context)
    

def product(request):
    context = dict()
    context['items'] = Item.objects.all()[0:8]
    return render(request,'product.html',context)


class CategoryView(View):
    def get(self, request, slug):
        category = Category.objects.all()
        products = Item.objects.filter(category__slug = slug)

        context = {
            'category': category,
            'products':products,
         }
        return render(request, 'product.html', context)

    