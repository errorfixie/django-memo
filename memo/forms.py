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
                    "class": "input-text-area",
                      "style" : "width:1300px; height:650px;font-size:15px"
                
                }
            ),
        }
        labels = {
            'title':"",
            'contents': '',
        }
