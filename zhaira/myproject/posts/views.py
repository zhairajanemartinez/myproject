from django.shortcuts import render
from .models import Posts # Import the Posts model

def post_list(request):
    post = Posts.objects.all()  # Fetch all posts from the database
    return render(request, 'posts/post_list.html', {'posts':
     post})  # Pass posts to the template
