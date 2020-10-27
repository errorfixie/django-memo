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
<<<<<<< HEAD
                attrs={
                    "class" : "input-text-area",
                    "onkeyup" : 'printName()',
                    "cols" : '100',
                    'rows' : '50',
=======
                attrs={ 
                    "class": "input-text-area",
                      "style" : "width:1300px; height:650px;font-size:15px"
                
>>>>>>> b33cf834c0648ec0a5dc07103e0db219965ac642
                }
            ),
        }
        labels = {
            'title':"",
            'contents': '',
        }
