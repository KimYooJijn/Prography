from django.db import models

# Create your models here.
class AddressBook(models.Model):
    name = models.CharField(max_length=25)
    company = models.CharField(max_length=50, blank=True)
    age = models.IntegerField(default=0)
    relation = models.CharField(max_length=25, blank=True)
    phone_addr = models.CharField(max_length=15)
    email = models.CharField(max_length=100, blank=True)
    brithday = models.DateField(blank=True)

# python manage.py makemigrations addrbook
#
# python manage.py migrate
