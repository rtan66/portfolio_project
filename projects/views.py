"""
a query is performed at line 35. A query is a 
command that allows you to create, retrieve, 
update or delete objects (or rows) in your 
database. In this case we retrieving all objects 
in. the projects table

In line 37 of the code block above, we define a 
dictionary context. The dictionary only has one 
entry projects to which we assign our Queryset 
containing all projects. The context dictionary 
is used to send information to our template. 
Every view function you create needs to have a 
context dictionary.


In line 38, context is added as an argument to 
render(). Any entries in the context dictionary 
are available in the template, as long as the 
context argument is passed to render(). You’ll 
need to create a context dictionary and pass 
it to render in each view function you create.

We also render a template named project_index.html, 
which doesn’t exist yet. Don’t worry about that 
for now. You’ll create the templates for these 
views in the next section.

"""


from django.shortcuts import render
from projects.models import Project

# Need to create the template project_detail.html
# Every view function you create needs to 
# have a context dictionary.
def project_index(request):
    
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    # A database query returns a collection of all
    # objects that match the query, known as the 
    # Queryset. 
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
    