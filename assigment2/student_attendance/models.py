from django.db import models

# Create your models here.
class User(models.Model):
    password = models.CharField(max_length= 15, default="changeme123")
    name = models.CharField(max_length= 50,  unique=True)
    security_question = models.CharField(max_length= 100, default="Your fav pet")
    security_answer = models.CharField(max_length= 100, default="dog")




    def __str__(self):
        return self.name
