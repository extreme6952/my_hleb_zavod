from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
from unidecode import unidecode
from inventory.models import Deportament


# Связь "один ко многим" в данном контексте означает, 
# что один экземпляр модели User (пользователь) 
# может быть связан с множеством экземпляров модели WorkSchedule (рабочие дни). 
# Это позволяет каждому пользователю создавать записи о своих 
# рабочих днях на разные даты
class WorkScheclude(models.Model):

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='work_scheclude_user')
    
    date = models.DateField(default=timezone.now)

    is_working = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.date} {'Рабочий' if self.is_working else 'Выходной'}"
    

#Будет профиль админа сайта,
#который сможет управлять контентом на сайте
class Profile(models.Model):

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profile_user')
    
    position = models.CharField(max_length=250)

    created = models.DateField(auto_now_add=True)

    updated = models.DateField(auto_now=True)

    image = models.ImageField(upload_to='%d/%m/%Y',
                              blank=True)

    def __str__(self):
        return f'Профиль работника "{self.user.last_name} {self.user.first_name}"'
    

class Profile_Company(models.Model):

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profile_company')
    
    created = models.DateField(auto_now_add=True)

    updated = models.DateField(auto_now=True)

    image = models.ImageField(upload_to='media_user_profile_company/%d/%m/%Y',
                              blank=True)