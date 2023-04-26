from django import forms
from .models import Note
from django.core.exceptions import ValidationError

class NotesForm(forms.ModelForm):
    class Meta:
        model=Note
        fields=('title','text')
        widgets= {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }
        labels= {
            'text': 'Write your thoughts here:'
        }

    #Validation example
    def clean_title(self):
        title = self.cleaned_data["title"]
        if 'Django' not in title:
            raise ValidationError('We only accept Notes about Django!')
        return title
        