from django import forms

from .models import Books


class BookCreate(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['name', 'photo', 'description', 'price', 'file']