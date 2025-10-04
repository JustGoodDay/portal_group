from django.urls import path
from .views import portfolio_list, portfolio_create, portfolio_edit, portfolio_delete

urlpatterns = [
    path('', portfolio_list, name='portfolio_list'),
    path('add/', portfolio_create, name='portfolio_create'),
    path('<int:pk>/edit/', portfolio_edit, name='portfolio_edit'),
    path('<int:pk>/delete/', portfolio_delete, name='portfolio_delete'),
]
