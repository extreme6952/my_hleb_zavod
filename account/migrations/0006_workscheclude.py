# Generated by Django 4.2.6 on 2025-01-08 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkScheclude',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('is_working', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_scheclude_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
