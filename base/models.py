from django.db import models

# Create your models here.
class Resume(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Email = models.EmailField()
    Phone = models.CharField(max_length=15)
    profilepic = models.ImageField(upload_to='profilepic', blank=True)
    about = models.TextField(blank=True)
    titles = models.CharField(max_length=50, blank=True)
    intro = models.TextField(blank=True)
    portfolio = models.ImageField(upload_to='portfolio', blank=True)


    def __str__(self):
        return self.Name