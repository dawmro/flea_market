from django.shortcuts import render, get_object_or_404, redirect
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
    # handle POST request
    if request.method == 'POST':
        # get form data and files uploaded by user
        form = NewItemForm(request.POST, request.FILES)
        # if there were no errors
        if form.is_valid():
            # create object but do not save it to db yet, because created_by field will not be added, and will result in error
            item = form.save(commit=False)
            # set created_by as currently logged in user
            item.created_by = request.user
            # now save it
            form.save()
            # return view and private key as id of item that just have been created
            return redirect('item:detail', pk=item.id)

    # handle GET request        
    else:
        form = NewItemForm()

        context = {
            'form': form,
            'title': 'New Item'
        }
        return render(request, 'item/form.html', context)


@login_required
def delete_item(request, pk):
    # get item from Item model using primary key from url and created by current user
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')

