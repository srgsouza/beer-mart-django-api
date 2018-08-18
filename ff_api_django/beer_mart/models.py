from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Beer(models.Model):
    brewery_name = models.CharField(max_length=100)
    beer_name = models.CharField(max_length=100)
    description = models.CharField(max_length=280)
    abv = models.IntegerField()
    price = models.IntegerField()
    package = models.CharField(max_length=100)
    user = models.ForeignKey('auth.User', related_name='beers', on_delete=models.CASCADE)

    def __str__(self):
        return self.beer_name

    def save(self, *args, **kwargs):
        super(Beer, self).save(*args, **kwargs)    
    
class Comment(models.Model):
    comment = models.CharField(max_length=280)
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment