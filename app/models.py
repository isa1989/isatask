from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import datetime


# Create your models here.



class Task(models.Model):
    user = models.ForeignKey(User, verbose_name='User', related_name='user',on_delete=models.CASCADE)
    other_user = models.ManyToManyField(User,related_name='other_user', verbose_name='Tapşırığı görsünlər', blank=True)
    comment_user = models.ManyToManyField(User, related_name='comment_user', verbose_name='Şərh yazsınlar', blank=True)
    name = models.CharField(max_length = 100, verbose_name='Tapşırığın adı')
    #slug = models.SlugField(max_length=122,unique=True, null = False, verbose_name='Slug',editable=False)
    description = models.TextField(verbose_name='Tapşırığın açıqlaması')
    end_time = models.DateTimeField(verbose_name='Tapşırığın bitmə tarixi')

    #end_time = models.DateField(auto_now=False)

    def __str__(self):
        return self.name





class Comment(models.Model):
    comm = models.ForeignKey(Task, verbose_name='Task', related_name='comment',on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='User', related_name='user_comments',on_delete=models.CASCADE)
    #comment_user = models.ManyToManyField(User, related_name='comment_user')
    description = models.TextField(max_length=300, verbose_name='Şərh yaz')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

