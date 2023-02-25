from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from item.models import Category, Item

from .forms import SignupForm

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


# signup view
def signup(request):

    if request.method == 'POST':
        # new instance of form and get all info from request
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/') 

    else:
        form = SignupForm()

    context = {
        'form': form
    }
    return render(request, 'core/signup.html', context)


# logout view
@login_required
def logout_view(request):
    logout(request)
    return redirect('/login/')
