from django.db import models

# To start the process of creating our database we need
# to create a migration.
# Migration is a file containing a Migrations class with
# rules that tells Django what changes need to be made to
# the database

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)        # name of the project
    description = models.TextField()                # description of the project
    technology = models.CharField(max_length=20)    # a selection of choices
    image = models.FilePathField(path='/img')       # image field that holds the image path