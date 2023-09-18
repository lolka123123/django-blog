from django.shortcuts import render, redirect
from .models import Article, Category, Profile, Comment
from django.urls import reverse_lazy
from django import forms

from .forms import LoginForm, RegistrationForm, CommentForm, ArticleForm, ProfileEditForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.views.generic import DeleteView, UpdateView
# from django.views.generic import ListView

def get_profile_image(request):
    for i in Profile.objects.all():
        if i.user.pk == request.user.pk:
            profile_image = i.image.url
            break
        else:
            profile_image = '/media/users/user.webp'
    return profile_image

def index(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    articles_lst = []
    for article in articles:
        articles_lst.append({
            'article': article,
            'categories': article.categories.all(),
            'profile': Profile.objects.get(user=article.creator.user),
            'comments': Comment.objects.filter(article=article),
            'comments_count': Comment.objects.filter(article=article).count()
        })

    profile_image = get_profile_image(request)

    context = {
        'title': 'Главная страница Блог',
        'categories': categories,
        'articles_lst': articles_lst,
        'profile_image': profile_image,
    }
    return render(request, 'blog/index.html', context)


def comment_delete(request, pk):
    comment = Comment.objects.get(pk=pk)

    if request.user.pk == comment.user.user.pk:
        comment.delete()

    return redirect('article', comment.article.pk)

def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        profile = Profile()
        if form.is_valid():
            username = request.POST.get('username')
            form.save()
            profile.user = User.objects.get(username=username)
            profile.save()
            return redirect('login')
        else:
            return redirect('register')
    else:
        form = RegistrationForm()

    context = {
        'title': 'Регистрация',
        'form': form,
    }
    return render(request, 'blog/user_form.html', context)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect('index')
            else:
                return redirect('login')
        else:
            return redirect('login')
    else:
        form = LoginForm()

    context = {
        'title': 'Вход в аккаунт',
        'form': form,
    }
    return render(request, 'blog/user_form.html', context)

def user_logout(request):
    logout(request)
    return redirect('index')

def user_profile(request, pk):
    profile_image = get_profile_image(request)

    user = User.objects.get(pk=pk)
    profile = Profile.objects.get(user=user)
    context = {
        'title': 'Профиль',
        'user': user,
        'profile': profile,
        'profile_image': profile_image,
    }
    return render(request, 'blog/profile.html', context)


def profile_edit(request, pk):
    profile_image = get_profile_image(request)

    user = User.objects.get(pk=pk)
    profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
        return redirect('profile', pk)
    else:
        form = ProfileEditForm(instance=profile)

    context = {
        'title': 'Редактировать профиль',
        'user': user,
        'profile': profile,
        'profile_image': profile_image,
        'form': form,
    }
    return render(request, 'blog/edit_profile.html', context)


def article_view(request, pk):
    article = Article.objects.get(pk=pk)
    profile = Profile.objects.get(user=article.creator.user)
    comments = Comment.objects.filter(article=article)
    profiles = Profile.objects.all()
    comments_count = comments.count()

    profile_image = get_profile_image(request)



    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = Profile.objects.get(user=request.user)
            comment.article = article

            comment.save()

            return redirect('article', article.pk)
        else:
            return redirect('article', article.pk)
    else:
        form = CommentForm()

    context = {
        'title': f'Статья: {article.title}',
        'article': article,
        'profile': profile,
        'profiles': profiles,
        'comments': comments,
        'form': form,
        'profile_image': profile_image,
        'comments_count': comments_count,
    }
    return render(request, 'blog/post.html', context)

# class ArticleUpdate(UpdateView):
#
#     model = Article
#     form_class = ArticleForm
#     template_name = 'blog/add_post.html'
#     extra_context = {
#         'title': 'Изменение статьи',
#     }

def add_article(request):
    profile_image = get_profile_image(request)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            article = form.save(commit=False)

            for profile in Profile.objects.all():
                if profile.user.pk == request.user.pk:
                    article.creator = profile

            article.save()
            return redirect('index')
        else:
            return redirect('add_article')
    else:
        form = ArticleForm()

    context = {
        'title': 'Добавить пост',
        'profile_image': profile_image,
        'form': form,

    }
    return render(request, 'blog/add_post.html', context)

def article_update(request, pk):
    profile_image = get_profile_image(request)
    article = Article.objects.get(pk=pk)

    if request.user.pk == article.creator.user.pk:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                article = form.save(commit=False)
                form.save_m2m()

                for profile in Profile.objects.all():
                    if profile.user.pk == request.user.pk:
                        article.creator = profile

                article.save()

                return redirect('index')
            else:
                return redirect('article_update', article.pk)
        else:
            form = ArticleForm(instance=article)

        context = {
            'title': 'Изменение статьи',
            'profile_image': profile_image,
            'article': article,
            'form': form,
        }
        return render(request, 'blog/add_post.html', context)

    else:
        return redirect('index')

def article_delete(request, pk):
    article = Article.objects.get(pk=pk)

    if request.user.pk == article.creator.user.pk:
        article.delete()

    return redirect('index')




class ArticleDelete(DeleteView):
    model = Article
    context_object_name = 'article'
    success_url = reverse_lazy('index')

def my_posts(request):
    profile_image = get_profile_image(request)

    articles = Article.objects.all()
    categories = Category.objects.all()
    articles_lst = []
    for article in articles:
        if article.creator.user.pk == request.user.pk:
            articles_lst.append({
                'article': article,
                'categories': article.categories.all(),
                'profile': Profile.objects.get(user=article.creator.user),
                'comments': Comment.objects.filter(user=article.creator),
                'comments_count': Comment.objects.filter(user=article.creator).count()
            })

    context = {
        'title': 'Мои посты',
        'profile_image': profile_image,
        'categories': categories,
        'articles_lst': articles_lst,
    }
    return render(request, 'blog/index.html', context)




def category(request, pk):
    profile_image = get_profile_image(request)
    articles = Article.objects.all()
    categories = Category.objects.all()
    category_title = Category.objects.get(pk=pk)
    articles_lst = []
    for article in articles:
        for category in article.categories.all():
            if category.pk == pk:
                articles_lst.append({
                    'article': article,
                    'categories': article.categories.all(),
                    'profile': Profile.objects.get(user=article.creator.user),
                    'comments': Comment.objects.filter(user=article.creator),
                    'comments_count': Comment.objects.filter(user=article.creator).count()
                })
                continue

    context = {
        'title': f'{category_title}',
        'profile_image': profile_image,
        'categories': categories,
        'articles_lst': articles_lst

    }
    return render(request, 'blog/index.html', context)