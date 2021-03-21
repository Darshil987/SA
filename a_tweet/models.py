from django.db import models


# Create your models here.
class InputData(models.Model):
    topic = models.CharField(max_length=100)
    no_tweets = models.PositiveIntegerField()

    pos = models.FloatField(blank=True, null=True)
    neg = models.FloatField(blank=True, null=True)
    neutral = models.FloatField(blank=True, null=True)
# polarity=models.FloatField(blank=True,null=True)
