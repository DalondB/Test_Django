from django.db import models

# Create your models here.
#Run whenever a change is made to database models
    #python manage.py makemigrations
    #python manage.py migrate

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)