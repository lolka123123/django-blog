# Generated by Django 4.2.4 on 2023-08-16 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_profile_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='users/user.webp', null=True, upload_to='users/', verbose_name='Изображение'),
        ),
    ]
