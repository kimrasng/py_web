from django import forms
from .models import Board

class BoardCreatrForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('title', 'file_upload', 'content')

class BoardUpdateForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('title', 'file_upload', 'content')