from django import forms

from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    # select model
    model = ConversationMessage
    # fields to use
    fields = ('content',)
    # do some styling
    widgets = {
        'content': forms.Textarea(attrs={
            'class': 'w-full py-4 px-6 rounded-xl border'
        })
    }