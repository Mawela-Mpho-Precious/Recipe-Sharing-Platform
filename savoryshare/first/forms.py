from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Recipe

from first.models import Recipe, Category


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter Password'}))

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with that email already exists.")
        return email


class CustomLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your email',
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter your password',
        'class': 'form-control'
    }))

class RecipeForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.filter(name__in=['Dessert', 'Lunch', 'Vegan', 'Dinner', 'Breakfast', 'Bakery']),
        empty_label="Select a category"
    )
    class Meta:
        model = Recipe
        fields = ['title', 'image', 'serves', 'cook_time', 'ingredients', 'instructions', 'category', 'locked']
        


from django import forms

RATING_CHOICES = [
    (1, '★☆☆☆☆'),
    (2, '★★☆☆☆'),
    (3, '★★★☆☆'),
    (4, '★★★★☆'),
    (5, '★★★★★'),
]

class RatingForm(forms.Form):
    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'star-rating'})
    )



