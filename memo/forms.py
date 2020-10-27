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
            "contents":forms.Textarea(
                attrs={
                    "class" : "input-text-area",
                    "onkeyup" : 'printName()',
                    "cols" : '100',
                    'rows' : '50',
                }
            ),
        }
        labels = {
            'title':"",
            'contents': '',
        }
