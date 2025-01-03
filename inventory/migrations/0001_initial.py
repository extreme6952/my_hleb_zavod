# Generated by Django 4.2.6 on 2024-12-14 17:41

from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(upload_to='product/%Y/%m/%d')),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(blank=True, max_length=250, unique=True)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(upload_to='product/%Y/%m/%d')),
                ('text', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('protein', models.PositiveIntegerField()),
                ('fat', models.PositiveIntegerField()),
                ('callories', models.PositiveIntegerField()),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.category')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['-name'], name='inventory_c_name_d55594_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['-created'], name='inventory_p_created_e283f3_idx'),
        ),
    ]
