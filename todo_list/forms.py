from django import forms
from .models import Todo

class AddNewTodo(forms.ModelForm):
    
    class Meta:
        model = Todo
        fields = [
            'title','description'
        ]
