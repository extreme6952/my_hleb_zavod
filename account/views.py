from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import timedelta,datetime
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
        obj = self.get_queryset().filter(user=self.request.user).first()
        print({obj})
        return obj

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
def add_work_date_user(request):
    #получаем текущую дату и время.
    today = datetime.today()
    #Устанавливает день текущей даты в 1, тем самым получая первый день текущего месяца.
    first_day_of_month = today.replace(day=1)
    #Для получения последнего дня месяца
    last_day_month = (first_day_of_month + timedelta(days=31)).replace(day=1) - timedelta(days=1)
    #Сначала добавляется 31 день к первому дню месяца (это гарантирует, что мы перейдем в следующий месяц).
    #Затем устанавливается день в 1, чтобы вернуться к первому дню следующего месяца.
    #Наконец, вычитается один день (timedelta(days=1)), чтобы получить последний день текущего месяца.
    
    if request.method=='POST':
        form = WorkSchecludeWorkDataForm(request.POST)
        if form.is_valid():
            work_scheclude = form.save(commit=False)
            work_scheclude.user = request.user
            work_scheclude.save()
            return redirect('account:profile_worker')
    else:
        form = WorkSchecludeWorkDataForm()

    work_days = WorkScheclude.objects.filter(user=request.user,
                                            date__range=[
                                                first_day_of_month,
                                                last_day_month
                                            ])

    word_days_dict = {day.date.strftime("%d/%m/%Y"):day.is_working for day in work_days}

    context = {
        'work_days_dict':word_days_dict,
        'form':form,
        'first_day_of_month':first_day_of_month,
        'last_day_of_month':last_day_month
    }

    return render(request,
                'profile/work_days.html',
                context)

