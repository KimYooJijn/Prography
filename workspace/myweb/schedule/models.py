from django.db import models

# Create your models here.
class Schdule(models.Model):
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=1000)
    flag = models.CharField(max_length=3)
    username = models.CharField(max_length=50)
    st_date = models.DateField()
    ed_date = models.DateField()
    st_time = models.TimeField()
    ed_time = models.TimeField()