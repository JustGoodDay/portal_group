from django.urls import path
from . import views

urlpatterns = [
    path('forum/', views.forum_list, name='forum_list'),
    path('forum/new/', views.forum_create, name='forum_create'),
    path('forum/vote/<int:post_id>/<int:vote>/', views.forum_vote, name='forum_vote'),

    path('complaints/', views.complaint_list, name='complaint_list'),
    path('complaints/new/', views.complaint_create, name='complaint_create'),
    path('complaints/vote/<int:complaint_id>/<int:vote>/', views.vote_complaint, name='vote_complaint'),
]
