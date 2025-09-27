from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .forms import ProfileCreationForm, StoryForm
from .models import Story

def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileCreationForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)

            return redirect("/") # на головну сторінку після реєстрації
    else:
        user_form = UserCreationForm()
        profile_form = ProfileCreationForm()

    context = {'user_form': user_form, 'profile_form': profile_form}

    return render(request, "authentication_app/register.html", context)

def logout_view(request):
    logout(request)
    return redirect('/register')


def gallery(request):
    form = StoryForm()
    if request.method == 'POST':
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')  # Перезагрузка страницы после загрузки
    stories = Story.objects.all()
    return render(request, 'authentication_app/gallery.html', {'stories': stories, 'form': form})





