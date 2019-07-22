from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class stuff(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField()
    owner = models.ForeignKey(User,default = None,  on_delete=models.CASCADE)
    price = models.IntegerField()
    commutative = models.BooleanField()
    markdown =  models.DecimalField(max_digits=2, decimal_places=0, null=True, blank=True)
    slug = models.SlugField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    category = models.CharField(max_length=1, choices=GENDER_CHOICES)
     