from django import forms
from django.forms import modelformset_factory
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import inlineformset_factory


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


class WorkSchecludeWorkDataForm(forms.ModelForm):
    class Meta:
        model = WorkScheclude
        fields = ['date','is_working']


#сделать методы для email
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','last_name','first_name','email']


class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']