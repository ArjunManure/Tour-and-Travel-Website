from django.db import models

# Create your models here.
class contact_view(models.Model):
    name = models.CharField(max_length = 122)
    email = models.CharField(max_length = 122)
    message = models.CharField(default="", max_length=50)
    
class register_view(models.Model):
    name = models.CharField(max_length = 122)
    email = models.CharField(max_length = 122)
    state = models.CharField(max_length = 122)
    city = models.CharField(max_length = 122)
    zipcode = models.IntegerField()
    suggestions = models.CharField(default="", max_length=50)
    