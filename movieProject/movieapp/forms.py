from .models import MovieTimes
from django import forms


class MovieForms(forms.ModelForm):
    class Meta:
        model = MovieTimes
        fields = ['name', 'desc', 'year', 'images']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Movie name'}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter description'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Released year'}),
            'images': forms.FileInput(attrs={'class': 'form-control'}),
        }
