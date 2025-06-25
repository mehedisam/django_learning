from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class StreamList(models.Model):
    name= models.CharField(max_length=100)
    about = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    website= models.URLField(max_length=100)
    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=100)
    storyLine = models.CharField(max_length=200)
    platform= models.ForeignKey(StreamList,on_delete=models.CASCADE, related_name='watchlist')
    active = models.BooleanField(default=True)
    avg_rating=models.FloatField(default=0)
    num_ratings=models.IntegerField(default=0)
    created= models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title

class Review(models.Model):
    review_user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    description=models.CharField(max_length=200,null=True)
    watchlist=models.ForeignKey(WatchList,on_delete=models.CASCADE,related_name='review')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return str(self.rating)+" - "+self.watchlist.title

