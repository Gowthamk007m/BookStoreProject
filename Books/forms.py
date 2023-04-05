from django import forms
from .models import Author, Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'sort',
                  'description', 'cover_image', 'pdf_file']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5})
        }


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio', 'image']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 5}),
        }
