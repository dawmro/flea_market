from django.shortcuts import render, get_object_or_404

from .models import Item

# Create your views here.

# detail view
def detail(request, pk):
    # get object from database, Item model, where primary key is pk
    item = get_object_or_404(Item, pk=pk)

    context = {
        'item': item
    }

    return render(request, 'item/detail.html', context)

