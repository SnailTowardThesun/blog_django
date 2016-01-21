from django.shortcuts import render

# Create your views here.
def homePage(request):
    return render(request,'index.html')
def aboutMe(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def post(request):
    return render(request,'post.html')
