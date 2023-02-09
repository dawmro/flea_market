from django.shortcuts import render

from item.models import Category, Item

# Create your views here.

# index view
def index(request):
    # get 6 first items that are not sold
    items = Item.objects.filter(is_sold=False)[:6]
    # from all categories
    categories = Category.objects.all()
    context = {
        'items': items,
        'categories': categories
    }

    return render(request, 'core/index.html', context)


# contact view
def contact(request):
    return render(request, 'core/contact.html')


# contact view
