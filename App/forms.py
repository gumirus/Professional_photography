from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваше имя'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваш email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваш номер телефона'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите ваш адрес'}),
            'answer': forms.Select(attrs={'class': 'form-control'}),
        }