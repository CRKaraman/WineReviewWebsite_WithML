from django.db import models
import numpy as np
from django.contrib.auth.models import User

# Create your models here.

class Wine(models.Model):
    name = models.CharField(max_length = 128)

    def average_rating(self):
        all_ratings = list(map(lambda x:x.rating,self.review_set.all()))
        return np.mean(all_ratings)

    def __str__(self):
        return self.name

class Review(models.Model):

    RATING_CHOICES = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
    )

    wine = models.ForeignKey(Wine, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(verbose_name='date_published')
    user_name = models.CharField(max_length = 100)
    comment = models.CharField(max_length = 200)
    rating = models.IntegerField(choices = RATING_CHOICES)

    def __str__(self):
        return self.comment

class Cluster(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

    def get_members(self):
        return "\n".join([u.username for u in self.users.all()])
