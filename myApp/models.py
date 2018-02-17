from django.db import models

from django.urls import reverse
import markdown
from django.utils.html import strip_tags

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
    # ... 其它已有字段
    # 新增 views 字段记录阅读量
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title



    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})



    def increase_views(self):
        self.views +=1
        self.save(update_fields=['views'])


    def save(self,*args,**kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extension_configs=[
                  'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])

            self.excerpt =strip_tags(md.convert(self.body))[:54]
        super(Post,self).save(*args,**kwargs)

    class Meta:
        ordering =['-created_time']