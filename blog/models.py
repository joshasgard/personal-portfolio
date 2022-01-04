from django.db import models
from datetime import date

class Myblogs(models.Model):
    # Creates Model class, called Project here, for inputting portolio projects as objects. 
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to = 'blog/images/', blank=True)
    url = models.URLField(blank=True)
    date = models.DateField(default = date.today)




