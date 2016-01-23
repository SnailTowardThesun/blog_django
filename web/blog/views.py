from django.shortcuts import render
from models import *
# Create your views here.
def homePage(request):
    # get top five blogs here
    latest_article = article.objects.order_by('-article_published_time')[:5]
    context = {'latest_article':latest_article}
    return render(request,'index.html',context)

def page_list(request,page_list_num):
    # get the blog begin with blog_begin_num
    list_article = article.objects.order_by('-article_published_time')[int(page_list_num) - 1:int(page_list_num) + 4]
    # get the number of all pages.
    # PS: the max size of blogs in one page is 5
    context = {'list_article':list_article}
    return render(request,'pagelist.html',context)

def article_page(request,article_file):
    # get comments here 
    return render(request,'BlogPages/' + article_file + '.html')


# static files
def aboutMe(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def post(request):
    return render(request,'post.html')
