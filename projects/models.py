from django.db import models

class Project(models.Model):
    # Creates Model class, called Project here, for inputting portolio projects as objects. 
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to = 'projects/images/')
    url = models.URLField(blank=True)


    
    def __str__(self):
        return self.title
