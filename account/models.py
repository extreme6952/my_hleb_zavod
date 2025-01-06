from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

#Будет профиль админа сайта,
#который сможет управлять контентом на сайте
class Profile(models.Model):

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profile_user')
    
    created = models.DateField(auto_now_add=True)

    updated = models.DateField(auto_now=True)

    image = models.ImageField(upload_to='%d/%m/%Y')

    def __str__(self):
        return f'Профиль работника "{self.user.last_name} {self.user.first_name}"'
    

class Profile_Company(models.Model):

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profile_company')
    
    created = models.DateField(auto_now_add=True)

    updated = models.DateField(auto_now=True)

    image = models.ImageField(upload_to='media_user_profile_company/%d/%m/%Y')