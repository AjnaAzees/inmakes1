from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    desc=models.TextField()
    def __str__(self):
        return self.name
class Team(models.Model):
    heading=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics')
    description=models.TextField()
    def __str__(self):
        return self.heading
