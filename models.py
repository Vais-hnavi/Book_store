from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Author(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)

    def fullname(self):
        return f'{self.fname}{self.lname}'
    
    def __str__(self):
        return self.fullname()


class Book(models.Model):
    title=models.CharField(max_length=20)
    rating=models.FloatField(validators=[MaxValueValidator(10),MinValueValidator(1)])
    author=models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    slug=models.SlugField(default='',null=False,blank=True)

    def __str__(self):
        return f'{self.title},ratings are {self.rating} and author is {self.author}'
    
    def get_absolute_url(self):
        return reverse('bd',args=[self.slug])

    #def save(self,*args,**kwargs):
    #    self.slug=slugify(self.title)
    #    super().save(*args,**kwargs)
        