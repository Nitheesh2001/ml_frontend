from django.db import models

# Create your models here.
class Details(models.Model):
    name = models.CharField( max_length=50)
    email = models.CharField( max_length=50)
    subject = models.TextField()

    def __str__(self) :
        return self.name