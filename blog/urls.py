from django.urls import path
from . import views

"""
before you get to create the templates and actually see this 
blog up and running is to hook up the URLs. You’ll need 
create another urls.py file inside blog/ and add the URLs 
for the three views:


Once the blog-specific URLs are in place, you need to add them 
to the PROJECTS URL configuration using include():

"""


urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("<category>/", views.blog_category, name="blog_category"),
]