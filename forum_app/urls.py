from forum_app import views as forum_views
from django.urls import path

urlpatterns = [
# Форум
    path('forum/', forum_views.forum_list, name='forum_list'),
    path('forum/new/', forum_views.forum_create, name='forum_create'),
# Жалобы
    path('complaints/', forum_views.complaint_list, name='complaint_list'),
    path('complaints/new/', forum_views.complaint_create, name='complaint_create'),
]
