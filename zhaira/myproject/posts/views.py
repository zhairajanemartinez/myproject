from django.shortcuts import render

def post_list(request):
    # Example data for posts
    posts = [
        {'title': 'First Post', 'content': 'This is the content of the first post.'},
        {'title': 'Second Post', 'content': 'This is the content of the second post.'},
        {'title': 'Third Post', 'content': 'This is the content of the third post.'},
    ]
    return render(request, 'posts/post_list.html', {'posts': posts})
