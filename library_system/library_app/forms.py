from django import forms
from .models import Book, TestResult

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class TestResultForm(forms.ModelForm):
    class Meta:
        model = TestResult
        fields = '__all__'
