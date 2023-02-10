from django.shortcuts import render, get_object_or_404

from .models import Item


# Create your views here.

# detail view
def detail(request, pk):
    # get object from database, Item model, where primary key is pk
    item = get_object_or_404(Item, pk=pk)
    # get another 3 items from the same category
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[:3]

    context = {
        'item': item,
        'related_items': related_items
    }

    return render(request, 'item/detail.html', context)




