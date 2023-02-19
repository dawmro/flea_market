from django import forms

from . models import Item


# tailwind classes to use
INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        # model to use
        model = Item
        # fields to use
        fields = ('category', 'name', 'description', 'price', 'image')

        # create widgets to override defaults
        widgets = {
            # add styling to make category select look better
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            # add styling to make name text input look better
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            # add styling to make description text area look better
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            # add styling to make price text input look better
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            # add styling to makeimage file input look better
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }
