from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def post_list(request):
    return render(request, 'posts/post_list.html')  # Render the post list template