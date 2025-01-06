from django import forms
from django.forms import modelformset_factory
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    
    image = forms.ImageField(required=False)
    email = forms.EmailField(required=True)
    
    class Meta:

        model = User
        fields = ['username','first_name','last_name','password1','password2']


    def clean_email(self):
        data = self.cleaned_data["email"]

        if User.objects.filter(email=data):

            raise forms.ValidationError('Данный e-mail уже существует.')
        
        return data
        
    def save(self,commit=True):

        user = super().save(commit=True)

        profile = Profile.objects.create(user=user,
                                         image=self.cleaned_data.get('image'))

        profile.save()

        return user