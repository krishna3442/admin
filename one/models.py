from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class User1(models.Model):


    full_name=models.CharField(max_length=254)
    last_name=models.CharField(max_length=254,default='')
    email = models.EmailField(max_length=70, unique= True)
    password = models.CharField(max_length=50,default='password')
    mobile_no=models.IntegerField()

    def __str__(self):
        return self.email
    def get_absolute_url(self):
        return reverse("one:detail",kwargs={'pk':self.pk})
