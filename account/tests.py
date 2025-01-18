from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile

class ProfileViewTest(TestCase):

    # Создается фиктивный пользователь
    def setUp(self):
        self.user = User.objects.create(username='testuser',
                                      password='testpass',
                                      last_name='Григорий',
                                      first_name='Казначеев')

        self.profile = Profile.objects.create(user=self.user,
                                           position='test-position')

    # Авторизация юзера
    def test_get_success_login(self):
        # Авторизуем юзера
        self.client.login(username='testuser', password='testpass')
        # Направляем юзера на страницу по url
        response = self.client.get(reverse('account:profile_worker'), follow=True)

        # Получаем контекст ответа
        context = response.context

        if context is None:
            print(f'Контекст данного шаблона отсутствует!, Статус код:{response.status_code}')
        else:
            user_profile = context.get('user_profile')

            if user_profile is not None:
                self.assertIsInstance(user_profile, Profile)
                self.assertEqual(user_profile, self.profile)
                print(f'Все данные юзера {user_profile} были правильно переданы в контекст')
            else:
                print(f'Объект user_profile не найден в контексте!{response.status_code}')

    def tearDown(self):
        self.user.delete()
        self.profile.delete()
