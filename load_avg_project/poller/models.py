from django.db import models

class LoadAvgSample(models.Model):
    timestamp = models.DateTimeField()
    one_minute = models.FloatField()
    five_minute = models.FloatField()
    fifteen_minute = models.FloatField()

class LoadAvgThreshold(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class LoadAvgEvent(models.Model):
    timestamp = models.DateTimeField()
    message = models.TextField()
    type = models.IntegerField()