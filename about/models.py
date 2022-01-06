from django.db import models
from datetime import date

class Aboutme(models.Model):
    # Creates Model class for about me here, for inputting portolio projects as objects. 
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(blank=True)
    date = models.DateField(default = date.today)


    def __str__(self):
        return self.title