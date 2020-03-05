from django.db import models
from django_summernote.fields import SummernoteTextField

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=250)
    username = models.CharField(max_length=50)
    content = SummernoteTextField(blank=True)
    b_type = models.CharField(max_length=2)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)
    view_cnt = models.IntegerField(default=0)
    good_cnt = models.IntegerField(default=0)
    bad_cnt = models.IntegerField(default=0)
    upload_file = models.FileField(null=True)


class BoardComment(models.Model):
    board_id = models.IntegerField()
    username = models.CharField(max_length=50)
    content = models.CharField(max_length=512)
    create_date = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)
