from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ForumPost, Complaint
from .forms import ForumPostForm, ComplaintForm


#Форум
def forum_list(request):
    posts = ForumPost.objects.all().order_by('-created_at')
    return render(request, 'forum_app/forum_list.html', {'posts': posts})


@login_required
def forum_create(request):
    if request.method == "POST":
        form = ForumPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('forum_list')
    else:
        form = ForumPostForm()
    return render(request, 'forum_app/forum_form.html', {'form': form})


#Жалобы
def complaint_list(request):
    complaints = Complaint.objects.all().order_by('-created_at')
    return render(request, 'forum_app/complaint_list.html', {'complaints': complaints})


@login_required
def complaint_create(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST, request.FILES)  # важно! для картинок
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.save()
            return redirect('complaint_list')
    else:
        form = ComplaintForm()
    return render(request, 'forum_app/complaint_form.html', {'form': form})
