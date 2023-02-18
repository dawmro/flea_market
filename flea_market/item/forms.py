from django import forms

from . models import Item


class NewItemForm(forms.ModelForm):
    class Meta:
        # model to use
        model = Item
        # fields to use
        fields = ('category', 'name', 'description', 'price', 'image')
