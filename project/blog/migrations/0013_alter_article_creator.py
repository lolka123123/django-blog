# Generated by Django 4.2.4 on 2023-08-16 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.profile', verbose_name='Пользователь'),
        ),
    ]
