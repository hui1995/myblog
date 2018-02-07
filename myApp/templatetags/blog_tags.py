from ..models import Post,Category


from django import template


register = template.Library #实例化

@register.simple_tag()#装饰器装饰
def get_recent_posts(num=5):

    return Post.objects.all().order_by('-created_time')[:num]



@register.simple_tag()
def archives():

    return Post.objects.dates('created_time','month',order='DESC')



@register.simple_tag()
def get_categories():

    return Category.objects.all()
