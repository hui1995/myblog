from django.db import models

from django.urls import reverse

from django.contrib.auth.models import  User

# Create your models here.

# 分类数据库表
class Category(models.Model):


    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


#     标签类
class Tag(models.Model):
    name =models.CharField(max_length=100)


    def __str__(self):
        return self.name



"""
文章类


@title：文章标题
@body：文章内容
@created_time：创建事件
@modified_time:最后修改事件
@excerpt：文章摘要
@category：关联分类
@tag：关联标签
@author：关联作者

"""

class Post(models.Model):




    title =models.CharField(max_length=70)
    body =models.TextField()
    created_time = models.DateTimeField()
    modified_time=models.DateTimeField()
    excerpt =models.CharField(max_length=200,blank=True)
    category=models.ForeignKey(Category)
    tags =models.ManyToManyField(Tag,blank=True)
    author =models.ForeignKey(User)

    def __str__(self):
        return self.title



    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})