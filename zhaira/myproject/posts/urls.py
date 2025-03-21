from django.urls import path
from . import views  # Corrected import

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
]