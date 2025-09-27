from django.urls import path
from . import views

urlpatterns = [
    path('', views.diary_view, name='diary_home'),
    path('<int:student_id>/', views.diary_view, name='diary'),
]