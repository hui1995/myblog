from django.contrib.syndication.views import Feed

from .models import Post
class AllPostsRssFeed(Feed):
    title ="辉博客"
    link='http://hui1995.com'
    description='技术开发博客'
    def items(self):
        return Post.objects.all()
    def item_title(self, item):
        return '[%s] %s' %(item.category,item.title)
    def item_description(self, item):
        return item.body