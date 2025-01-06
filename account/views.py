from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *


class UserRegistrationView(TemplateResponseMixin,View):

    template_name = 'registration/registration.html'

    def get_form(self,data=None,files=None):

        return UserRegistrationForm(data=data,
                                    files=files)
    
    def get(self,request,*args, **kwargs):

        form = self.get_form()

        return self.render_to_response({"form":form})
        
    def post(self,request,*args, **kwargs):

        form = self.get_form(data=request.POST,
                             files=request.FILES)
        
        if form.is_valid():

            new_user = form.save(commit=False)

            new_user.set_password(form.cleaned_data['password1'])

            new_user.save()

            return redirect('account:login')
        
        return self.render_to_response(
            {"form":form,},
            )
    

class ProfileUserDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile/profile_detail_user.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        # Получаем профиль текущего пользователя
        return self.get_queryset().filter(user=self.request.user).first()