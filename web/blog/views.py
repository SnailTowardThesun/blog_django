from django.shortcuts import render
from models import *


# Create your views here.
def homepage(request):
    # get top five blogs here
    latest_article = Article.objects.order_by('-article_published_time')[:5]
    context = {'latest_article': latest_article}
    return render(request, 'blog/index.html', context)


def page_list(request, page_list_num):
    # get the blog begin with blog_begin_num
    i_page_num = int(page_list_num)
    list_article = Article.objects.order_by('-article_published_time')[(i_page_num - 1) * 2:(i_page_num - 1) * 2 + 2]
    # get the number of all pages.
    # PS: the max size of blogs in one page is 5
    list_page = range(1, int(Article.objects.count() / 2) + 2)
    context = {
        'list_article': list_article,
        'list_page': list_page,
    }
    return render(request, 'blog/pagelist.html', context)


def article_page(request, article_file):
    # get comments here 
    return render(request, 'blog/BlogPages/' + article_file + '.html')


# static files
def aboutMe(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')


def post(request):
    return render(request, 'blog/post.html')
