"""
blog_index will display a list of all your posts.

blog_detail will display the full post as well as 
comments and a form to allow users to create new comments.

blog_category will be similar to blog_index, but the posts 
viewed will only be of a specific category chosen by the user.

We then go on to check if a POST request has been received. 
If it has, then we create a new instance of our form, 
populated with the data entered into the form.

The form is then validated using is_valid(). If the form 
is valid, a new instance of Comment is created. You can 
access the data from the form using form.cleaned_data, 
which is a dictionary.

They keys of the dictionary correspond to the form fields, 
so you can access the author using 

    form.cleaned_data['author']. 

Don’t forget to add the current post to the comment
 when you create it.





"""

from django.shortcuts import render
from blog.models import Post, Comment
from .forms import CommentForm

def blog_index(request):
    """
        blog_index will display a list of all your posts.
        
        posts is a Queryset with all the posts 
        in the database

    """
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)


def blog_category(request, category):
    """
    we only want posts whose categories 
    contain the category with the name 
    corresponding to that given in the 
    argument of the view function. 
    Again, you’re using order_by() 
    to order posts starting with the 
    most recent.

    blog_category will be similar to 
    blog_index, but the posts viewed will 
    only be of a specific category chosen by the user.


    We then add these posts and the category 
    to the context dictionary, and render 
    our template.
    """
    posts = Post.objects.filter(
        categories__name__contains=category
        ).order_by('-created_on')
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)


def blog_detail(request, pk):
    """
    blog_detail will display the full post as well 
    as comments and a form to allow users to create 
    new comments.

    function takes a pk value as an argument 
    and, retrieves the object with the given pk.

    add both post and comments to the context 
    dictionary and render the template.
    """
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()


    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, "blog_detail.html", context)