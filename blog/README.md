Don’t forget to add blog to your INSTALLED_APPS in personal_porfolio/settings.py

Hold off on hooking up the URLs for now. As with the projects app, you’ll start by adding your models.

*******************Blog App: Models********************¨

$ python manage.py startapp blog
This may start to feel familiar to you, as its your third time doing this. Don’t forget to add blog to your INSTALLED_APPS in personal_porfolio/settings.py:

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "projects",
    "blog",
]
Hold off on hooking up the URLs for now. As with the projects app, you’ll start by adding your models.

Blog App: Models
The models.py file in this app is much more complicated than in the projects app.

You’re going to need three separate database tables for the blog:

Post
Category
Comment
These tables need to be related to one another. This is made easier because Django models come with fields specifically for this purpose.

Below is the code for the Category and Post models:

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
The Category model is very simple. All that’s needed is a single CharField in which we store the name of the category.

The title and body fields on the Post model are the same field types as you used in the Project model. We only need a CharField for the title as we only want a short string for the post title. The body needs to be a long-form piece of text, so we use a TextField.

The next two fields, created_on and last_modified, are Django DateTimeFields. These store a datetime object containing the date and time when the post was created and modified respectively.

On line 9, the DateTimeField takes an argument auto_now_add=True. This assigns the current date and time to this field whenever an instance of this class is created.

On line 10, the DateTimeField takes an argument auto_now=True. This assigns the current date and time to this field whenever an instance of this class is saved. That means whenever you edit an instance of this class, the date_modified is updated.

The final field on the post model is the most interesting. We want to link our models for categories and posts in such a way that many categories can be assigned to many posts. Luckily, Django makes this easier for us by providing a ManytoManyField field type. This field links the Post and Category models and allows us to create a relationship between the two tables.

The ManyToManyField takes two arguments. The first is the model with which the relationship is, in this case its Category. The second allows us to access the relationship from a Category object, even though we haven’t added a field there. By adding a related_name of posts, we can access category.posts to give us a list of posts with that category.

The third and final model we need to add is Comment. We’ll use another relationship field similar the ManyToManyField that relates Post and Category. However, we only want the relationship to go one way: one post should have many comments.

You’ll see how this works after we define the Comment class:

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)


The first three fields on this model should look familiar. There’s an author field for users to add a name or alias, a body field for the body of the comment, and a created_on field that is identical to the created_on field on the Post model.

On line 20, we use another relational field, the ForeignKey field. This is similar to the ManyToManyField but instead defines a many to one relationship. The reasoning behind this is that many comments can be assigned to one post. But you can’t have a comment that corresponds to many posts.

The ForeignKey field takes two arguments. The first is the other model in the relationship, in this case, Post. The second tells Django what to do when a post is deleted. If a post is deleted, then we don’t want the comments related to it hanging around. We, therefore, want to delete them as well, so we add the argument on_delete=models.CASCADE.

Once you’ve created the models, you can create the migration files with makemigrations:

$ python manage.py makemigrations blog

The final step is to migrate the tables. This time, don’t add the app-specific flag. Later on, you’ll need the User model that Django creates for you:

$ python manage.py migrate

Now that you’ve created the models, we can start to add some posts and categories. You won’t be doing this from the command line as you did with the projects, as typing out a whole blog post into the command line would be unpleasant to say the least!

Instead, you’ll learn how to use the Django Admin, which will allow you to create instances of your model classes in a nice web interface.

Don’t forget that you can check out the source code for this section on GitHub before moving onto the next section.


 
****************Blog App: Django Admin*****************

The Django Admin is a fantastic tool and one of the great benefits of using Django. As you’re the only person who’s going to be writing blog posts and creating categories, there’s no need to create a user interface to do so.

On the other hand, you don’t want to have to write blog posts in the command line. This is where the admin comes in. It allows you to create, update, and delete instances of your model classes and provides a nice interface for doing so.

Before you can access the admin, you need to add yourself as a superuser. This is why, in the previous section, you applied migrations project-wide as opposed to just for the app. Django comes with built-in user models and a user management system that will allow you to login to the admin.

To start off, you can add yourself as superuser using the following command:

$ python manage.py createsuperuser


You’ll then be prompted to enter a username followed by your email address and password. Once you’ve entered the required details, you’ll be notified that the superuser has been created. Don’t worry if you make a mistake since you can just start again:

    Username (leave blank to use 'jasmine'): jfiner
    Email address: jfiner@example.com
    Password:
    Password (again):
    Superuser created successfully.
    Navigate to localhost:8000/admin and log in with the credentials you just used to create a superuser. You’ll see a page similar to the one below:

The Default Django Admin
The User and Groups models should appear, but you’ll notice that there’s no reference to the models you’ve created yourself. That’s because you need to register them inside the admin.

In the blog directory, open the file admin.py and type the following lines of code:

from django.contrib import admin
from blog.models import Post, Category

class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
On line 2, you import the models you want to register on the admin page.

Note: We’re not adding the comments to the admin. That’s because it’s not usually necessary to edit or create comments yourself.

If you wanted to add a feature where comments are moderated, then go ahead and add the Comments model too. The steps to do so are exactly the same!

On line 4 and line 7, you define empty classes PostAdmin and CategoryAdmin. For the purposes of this tutorial, you don’t need to add any attributes or methods to these classes. They are used to customize what is shown on the admin pages. For this tutorial, the default configuration is enough.

The last two lines are the most important. These register the models with the admin classes. If you now visit localhost:8000/admin, then you should see that the Post and Category models are now visible:

Django Admin with Posts and Categories
If you click into Posts or Categorys, you should be able to add new instances of both models. I like to add the text of fake blog posts by using lorem ipsum dummy text.

Create a couple of fake posts and assign them fake categories before moving onto the next section. That way, you’ll have posts you can view when we create our templates.

Don’t forget to check out the source code for this section before moving on to building out the views for our app.


 Remove ads
Blog App: Views
You’ll need to create three view functions in the views.py file in the blog directory:

blog_index will display a list of all your posts.
blog_detail will display the full post as well as comments and a form to allow users to create new comments.
blog_category will be similar to blog_index, but the posts viewed will only be of a specific category chosen by the user.
The simplest view function to start with is blog_index(). This will be very similar to the project_index() view from your project app. You’ll just query the Post models and retrieve all its objects:

from django.shortcuts import render
from blog.models import Post, Comment

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)
On line 2, you import the Post and the Comment models, and on line 5 inside the view function, you obtain a Queryset containing all the posts in the database. order_by() orders the Queryset according to the argument given. The minus sign tells Django to start with the largest value rather than the smallest. We use this, as we want the posts to be ordered with the most recent post first.

Finally, you define the context dictionary and render the template. Don’t worry about creating it yet. You’ll get to creating those in the next section.

Next, you can start to create the blog_category() view. The view function will need to take a category name as an argument and query the Post database for all posts that have been assigned the given category:

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)
On line 14, you’ve used a Django Queryset filter. The argument of the filter tells Django what conditions need to be met for an object to be retrieved. In this case, we only want posts whose categories contain the category with the name corresponding to that given in the argument of the view function. Again, you’re using order_by() to order posts starting with the most recent.

We then add these posts and the category to the context dictionary, and render our template.

The last view function to add is blog_detail(). This is more complicated as we are going to include a form. Before you add the form, just set up the view function to show a specific post with a comment associated with it. This function will be almost equivalent to the project_detail() view function in the projects app:

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }

    return render(request, "blog_detail.html", context)
The view function takes a pk value as an argument and, on line 22, retrieves the object with the given pk.

On line 23, we retrieve all the comments assigned to the given post using Django filters again.

Lastly, add both post and comments to the context dictionary and render the template.

To add a form to the page, you’ll need to create another file in the blog directory named forms.py. Django forms are very similar to models. A form consists of a class where the class attributes are form fields. Django comes with some built-in form fields that you can use to quickly create the form you need.

For this form, the only fields you’ll need are author, which should be a CharField, and body, which can also be a CharField.

Note: If the CharField of your form corresponds to a model CharField, make sure both have the same max_length value.

blog/forms.py should contain the following code:

from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )
You’ll also notice an argument widget has been passed to both the fields. The author field has the forms.TextInput widget. This tells Django to load this field as an HTML text input element in the templates. The body field uses a forms.TextArea widget instead, so that the field is rendered as an HTML text area element.

These widgets also take an argument attrs, which is a dictionary and allows us to specify some CSS classes, which will help with formatting the template for this view later. It also allows us to add some placeholder text.

When a form is posted, a POST request is sent to the server. So, in the view function, we need to check if a POST request has been received. We can then create a comment from the form fields. Django comes with a handy is_valid() on its forms, so we can check that all the fields have been entered correctly.

Once you’ve created the comment from the form, you’ll need to save it using save() and then query the database for all the comments assigned to the given post. Your view function should contain the following code:

def blog_detail(request, pk):
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
On line 24, we create an instance of our form class. Don’t forget to import your form at the beginning of the file:

from .forms import CommentForm
We then go on to check if a POST request has been received. If it has, then we create a new instance of our form, populated with the data entered into the form.

The form is then validated using is_valid(). If the form is valid, a new instance of Comment is created. You can access the data from the form using form.cleaned_data, which is a dictionary.

They keys of the dictionary correspond to the form fields, so you can access the author using form.cleaned_data['author']. Don’t forget to add the current post to the comment when you create it.

Note: The life cycle of submitting a form can be a little complicated, so here’s an outline of how it works:

When a user visits a page containing a form, they send a GET request to the server. In this case, there’s no data entered in the form, so we just want to render the form and display it.
When a user enters information and clicks the Submit button, a POST request, containing the data submitted with the form, is sent to the server. At this point, the data must be processed, and two things can happen:
The form is valid, and the user is redirected to the next page.
The form is invalid, and empty form is once again displayed. The user is back at step 1, and the process repeats.
The Django forms module will output some errors, which you can display to the user. This is beyond the scope of this tutorial, but you can read more about rendering form error messages in the Django documentation.

On line 33, save the comment and go on to add the form to the context dictionary so you can access the form in the HTML template.

The final step before you get to create the templates and actually see this blog up and running is to hook up the URLs. You’ll need create another urls.py file inside blog/ and add the URLs for the three views:

from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("<category>/", views.blog_category, name="blog_category"),
]
Once the blog-specific URLs are in place, you need to add them to the projects URL configuration using include():

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("projects/", include("projects.urls")),
    path("blog/", include("blog.urls")),
]
With this set up, all the blog URLs will be prefixed with blog/, and you’ll have the following URL paths:

localhost:8000/blog: Blog index
localhost:8000/blog/1: Blog detail view of blog with pk=1
localhost:8000/blog/python: Blog index view of all posts with category python
These URLs won’t work just yet as you still need to create the templates.

In this section, you created all the views for your blog application. You learned how to use filters when making queries and how to create Django forms. It won’t be long now until you can see your blog app in action!

As always, don’t forget that you can check out the source code for this section on GitHub.

Blog App: Templates
The final piece of our blog app is the templates. By the end of this section, you’ll have created a fully functioning blog.

You’ll notice there are some bootstrap elements included in the templates to make the interface prettier. These aren’t the focus of the tutorial so I’ve glossed over what they do but do check out the Bootstrap docs to find out more.

The first template you’ll create is for the blog index in a new file blog/templates/blog_index.html. This will be very similar to the projects index view.

You’ll use a for loop to loop over all the posts. For each post, you’ll display the title and a snippet of the body. As always, you’ll extend the base template personal_porfolio/templates/base.html, which contains our navigation bar and some extra formatting:

{% extends "base.html" %}
{% block page_content %}
<div class="col-md-8 offset-md-2">
    <h1>Blog Index</h1>
    <hr>
    {% for post in posts %}
    <h2><a href="{% url 'blog_detail' post.pk%}">{{ post.title }}</a></h2>
    <small>
        {{ post.created_on.date }} |&nbsp;
        Categories:&nbsp;
        {% for category in post.categories.all %}
        <a href="{% url 'blog_category' category.name %}">
            {{ category.name }}
        </a>&nbsp;
        {% endfor %}
    </small>
    <p>{{ post.body | slice:":400" }}...</p>
    {% endfor %}
</div>
{% endblock %}
On line 7, we have the post title, which is a hyperlink. The link is a Django link where we are pointing to the URL named blog_detail, which takes an integer as its argument and should correspond to the pk value of the post.

Underneath the title, we’ll display the created_on attribute of the post as well as its categories. On line 11, we use another for loop to loop over all the categories assigned to the post.

On line 17, we use a template filter slice to cut off the post body at 400 characters so that the blog index is more readable.

Once that’s in place, you should be able to access this page by visiting localhost:8000/blog:

Blog Index View
Next, create another HTML file blog/templates/blog_category.html where your blog_category template will live. This should be identical to blog_index.html, except with the category name inside the h1 tag instead of Blog Index:

{% extends "base.html" %}
{% block page_content %}
<div class="col-md-8 offset-md-2">
    <h1>{{ category | title }}</h1>
    <hr>
    {% for post in posts %}
        <h2><a href="{% url 'blog_detail' post.pk%}">{{ post.title }}</a></h2>
        <small>
            {{ post.created_on.date }} |&nbsp;
            Categories:&nbsp;
            {% for category in post.categories.all %}
            <a href="{% url 'blog_category' category.name %}">
                {{ category.name }}
            </a>&nbsp;
            {% endfor %}
        </small>
        <p>{{ post.body | slice:":400" }}...</p>
    {% endfor %}
</div>
{% endblock %}
Most of this template is identical to the previous template. The only difference is on line 4, where we use another Django template filter title. This applies titlecase to the string and makes words start with an uppercase character.

With that template finished, you’ll be able to access your category view. If you defined a category named python, you should be able to visit localhost:8000/blog/python and see all the posts with that category:

Blog Category View
The last template to create is the blog_detail template. In this template, you’ll display the title and full body of a post.

Between the title and the body of the post, you’ll display the date the post was created and any categories. Underneath that, you’ll include a comments form so users can add a new comment. Under this, there will be a list of comments that have already been left:

{% extends "base.html" %}
{% block page_content %}
<div class="col-md-8 offset-md-2">
    <h1>{{ post.title }}</h1>
    <small>
        {{ post.created_on.date }} |&nbsp;
        Categories:&nbsp;
        {% for category in post.categories.all %}
        <a href="{% url 'blog_category' category.name %}">
            {{ category.name }}
        </a>&nbsp;
        {% endfor %}
    </small>
    <p>{{ post.body | linebreaks }}</p>
    <h3>Leave a comment:</h3>
    <form action="/blog/{{ post.pk }}/" method="post">
        {% csrf_token %}
        <div class="form-group">
            {{ form.author }}
        </div>
        <div class="form-group">
            {{ form.body }}
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
    <h3>Comments:</h3>
    {% for comment in comments %}
    <p>
        On {{comment.created_on.date }}&nbsp;
        <b>{{ comment.author }}</b> wrote:
    </p>
    <p>{{ comment.body }}</p>
    <hr>
    {% endfor %}
</div>
{% endblock %}
The first few lines of the template in which we display the post title, date, and categories is the same logic as for the previous templates. This time, when rendering the post body, use a linebreaks template filter. This tag registers line breaks as new paragraphs, so the body doesn’t appear as one long block of text.

Underneath the post, on line 16, you’ll display your form. The form action points to the URL path of the page to which you’re sending the POST request to. In this case, it’s the same as the page that is currently being visited. You then add a csrf_token, which provides security and renders the body and author fields of the form, followed by a submit button.

To get the bootstrap styling on the author and body fields, you need to add the form-control class to the text inputs.

Because Django renders the inputs for you when you include {{ form.body }} and {{ form.author }}, you can’t add these classes in the template. That’s why you added the attributes to the form widgets in the previous section.

Underneath the form, there’s another for loop that loops over all the comments on the given post. The comments, body, author, and created_on attributes are all displayed.

Once that template is in place, you should be able to visit localhost:8000/blog/1 and view your first post:

Blog Detail View
You should also be able to access the post detail pages by clicking on their title in the blog_index view.

The final finishing touch is to add a link to the blog_index to the navigation bar in base.html. This way, when you click on Blog in the navigation bar, you’ll be able to visit the blog. Check out the updates to base.html in the source code to see how to add that link.

With that now in place, your personal portfolio site is complete, and you’ve created your first Django site. The final version of the source code containing all the features can be found on GitHub, so check it out! Click around the site a bit to see all the functionality and try leaving some comments on your posts!

You may find a few things here and there that you think need polishing. Go ahead and tidy them up. The best way to learn more about this web framework is through practice, so try to extend this project and make it even better! If you’re not sure where to start, I’ve left a few ideas for you in the conclusion below!

Conclusion
Congratulations, you’ve reached the end of the tutorial! We’ve covered a lot, so make sure to keep practicing and building. The more you build the easier it will become and the less you’ll have to refer back to this article or the documentation. You’ll be building sophisticated web applications in no time.

In this tutorial you’ve seen:

How to create Django projects and apps
How to add web pages with views and templates
How to get user input with forms
How to hook your views and templates up with URL configurations
How to add data to your site using relational databases with Django’s Object Relational Mapper
How to use the Django Admin to manage your models
In addition, you’ve learned about the MVT structure of Django web applications and why Django is such a good choice for web development.

If you want to learn more about Django, do check out the documentation and make sure to check out Part 2 of this series!










Note: The life cycle of submitting a form can be a little complicated, so here’s an outline of how it works:

When a user visits a page containing a form, they send a GET request to the server. In this case, there’s no data entered in the form, so we just want to render the form and display it.

When a user enters information and clicks the Submit button, a POST request, containing the data submitted with the form, is sent to the server. At this point, the data must be processed, and two things can happen:

The form is valid, and the user is redirected to the next page.

The form is invalid, and empty form is once again displayed. The user is back at step 1, and the process repeats.