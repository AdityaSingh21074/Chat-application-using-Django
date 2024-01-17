# forms.py
from django import forms
from .models import Room

from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Your message...', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'class': 'form-control'})
        
class CreateRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'slug']  