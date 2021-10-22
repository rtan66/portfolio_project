"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# here we do the final step
# hook up the projects urls.py 
# we need to include a URL configuration for the hello_world app
# This looks for a module called urls.py inside hello_world application
# and registers any URL defined there.
# Whenever you visit the root path of your URL (localhost:8000)
# the hello_world applications URLs will be registered.
"""
The line 44 of code includes all the URLs in the 
projects app but means they are accessed when 
prefixed by projects/. There are now two 
full URLs that can be accessed with our project:

localhost:8000/projects: The project index page
localhost:8000/projects/3: The detail view 
for the project with pk=3

These URLs still won’t work properly because 
we don’t have any HTML templates.


"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("projects/", include("projects.urls")),
]
