from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$',views.homePage,name='index'),
        url(r'^index',views.homePage,name='index'),
        url(r'^about',views.aboutMe,name='abhout'),
        url(r'^contact',views.contact,name='contact'),
        url(r'^post',views.post,name='post'),
        url(r'^article/(?P<article_file>\w+)/$',views.article_page,name='article_detail'),
		url(r'^page(?P<page_list_num>\w+)/$',views.page_list,name='get_page_list'),
        ]
