from django.shortcuts import render

def index(request):
    return render (request,'Home.html')
def About(request):
    return render (request,'About.html')
def Skills(request):
    return render (request,'Skills.html')
def Contact(request):
    return render (request,'Contact.html')
