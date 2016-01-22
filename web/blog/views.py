from django.shortcuts import render

# Create your views here.
def homePage(request):
    # get blog lists here 
    return render(request,'index.html')

def article(request,article_file):
    # get comments here 
    return render(request,'BlogPages/' + article_file + '.html')


# static files
def aboutMe(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def post(request):
    return render(request,'post.html')
