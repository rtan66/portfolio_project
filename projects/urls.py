from django.urls import path
from . import views


"""
In line 5, we hook up the root URL of our app 
to the project_index view. It is slightly more 
complicated to hook up the project_detail view. 
To do this, we want the URL to be /1, or /2, and 
so on, depending on the pk of the project.

The pk value in the URL is the same pk passed to 
the view function, so you need to dynamically generate 
these URLs depending on which project you want to view. 
To do this, we used the <int:pk> notation. This just 
tells Django that the value passed in the URL is an 
integer, and its variable name is pk.

With those now set up, we need to hook these URLs up to 
the project URLs. In personal_portfolio/urls.py, add the 
following highlighted line of code:
 path("projects/", include("projects.urls")),

"""



urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]