from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ForumPost, ForumPostLike, Complaint, Like
from .forms import ForumPostForm, ComplaintForm


# Форум
def forum_list(request):
    posts = ForumPost.objects.all().order_by('-created_at')
    posts_data = []

    for post in posts:
        likes_count = post.likes.filter(is_like=True).count()
        dislikes_count = post.likes.filter(is_like=False).count()
        user_vote = None
        if request.user.is_authenticated:
            uv = post.likes.filter(user=request.user).first()
            if uv:
                user_vote = uv.is_like

        posts_data.append({
            'post': post,
            'likes_count': likes_count,
            'dislikes_count': dislikes_count,
            'user_vote': user_vote,
        })

    return render(request, 'forum_app/forum_list.html', {'posts_data': posts_data})


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


@login_required
def forum_vote(request, post_id, vote):
    post = get_object_or_404(ForumPost, id=post_id)
    like, created = ForumPostLike.objects.get_or_create(
        post=post,
        user=request.user,
        defaults={'is_like': False}
    )
    like.is_like = True if vote == 1 else False
    like.save()
    return redirect('forum_list')


# Скарги
def complaint_list(request):
    complaints = Complaint.objects.all().order_by('-created_at')

    user_likes = {
        like.complaint_id: like.is_like
        for like in Like.objects.filter(user=request.user)
    } if request.user.is_authenticated else {}

    likes_count = {c.id: c.likes.filter(is_like=True).count() for c in complaints}
    dislikes_count = {c.id: c.likes.filter(is_like=False).count() for c in complaints}

    return render(request, 'forum_app/complaint_list.html', {
        'complaints': complaints,
        'user_likes': user_likes,
        'likes_count': likes_count,
        'dislikes_count': dislikes_count,
    })


@login_required
def complaint_create(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.save()
            return redirect('complaint_list')
    else:
        form = ComplaintForm()
    return render(request, 'forum_app/complaint_form.html', {'form': form})


@login_required
def vote_complaint(request, complaint_id, vote):
    complaint = get_object_or_404(Complaint, id=complaint_id)
    like, created = Like.objects.get_or_create(
        complaint=complaint,
        user=request.user,
        defaults={'is_like': False}
    )
    like.is_like = True if vote == 1 else False
    like.save()
    return redirect('complaint_list')
