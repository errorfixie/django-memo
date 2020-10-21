from django import forms
from . import models

class MemoCreateForm(forms.ModelForm):
    class Meta:
        model = models.Memo
        
        fields = [
            "contents"
        ]

        widgets = {
            "contents":forms.Textarea(
                attrs={ 
                    "class": "input-text-area",
                
                }
            ),
        }
        labels = {
            'contents': '',
        }
