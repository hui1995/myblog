from django.conf.urls import url


from . import views
from myApp.feeds import AllPostsRssFeed




app_name='blog'


urlpatterns =[


    url(r'^$',views.IndexView.as_view(),name='index'),

    url(r'^post/(?P<pk>[0-9]+)/$',views.PostDetailView.as_view(),name='detail'),

    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.ArchivesView.as_view(),name='archive'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    url(r'^all/rss/$',AllPostsRssFeed(),name='rss'),
    url(r'^search/$', views.search, name='search'),
    url(r'^about/$',views.about,name='about'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^blog/$',views.full_widthView.as_view(),name='full')
]