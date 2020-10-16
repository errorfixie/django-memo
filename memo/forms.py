from django import forms
from . import models

class MemoCreateForm(forms.ModelForm):
    class Meta:
        model = models.Memo
        
        fields = [
            "title",
            "contents"
        ]

        widgets = {
            "title":forms.TextInput(),
            "contents":forms.Textarea(),
        }