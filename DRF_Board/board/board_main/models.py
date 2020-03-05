from django.db import models

# Create your models here.
class Boardlist(models.Model):
    id = models.AutoField(db_column='NO', primary_key = True)
    pcode = models.CharField(db_column='PCODE', max_length=4)
    user_id= models.CharField(db_column='USER_ID', max_length=50, blank=True, null=True)
    title=models.CharField(db_column='TITLE', max_length=100 )
    content= models.CharField(db_column='CONTENT', max_length=1000, blank=True, null=True)
    priority = models.IntegerField(db_column='PRIORITY', blank=True, null=True)
    date=models.DateField(db_column='DATE', auto_now_add=True, blank=True, null=True )

    