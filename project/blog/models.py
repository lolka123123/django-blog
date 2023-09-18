from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название категории')

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категирия'
        verbose_name_plural = 'Категирии'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    image = models.ImageField(upload_to='users/',
                              null=True, blank=True,
                              default='users/user.webp',
                              verbose_name='Изображение')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок статьи')
    description = models.TextField(default='Здесь будет текст', verbose_name='Описание')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    categories = models.ManyToManyField(Category, verbose_name='Категории')
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Пользователь')


    def get_absolute_url(self):
        return reverse('article', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Пользователь')
    text = models.CharField(max_length=255, verbose_name='Текст')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.user.user.username

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


