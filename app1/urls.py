from django.urls import path
from . import views

urlpatterns = [
    path('', views.player_list, name='player_list'),
    path('add/', views.add_player, name='add_player'),
    path('update/<int:id>/', views.update_player, name='update_player'),
    path('delete/<int:id>/', views.delete_player, name='delete_player'),
]