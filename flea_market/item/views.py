from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Item
from .forms import NewItemForm


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


# new item view
@login_required
def new_item(request):
    form = NewItemForm()

    context = {
        'form': form,
        'title': 'New Item'
    }
    return render(request, 'item/form.html', context)




