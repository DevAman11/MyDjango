from django.shortcuts import render,HttpResponse


def index(req):
    data={"age":[3,5,7,8]}
    return render(req,'index.html',context=data)

def dynamic(req,id):
    return render(req,id)

def Home(req):
    return render(req,"Home.html")

def Blog(req):
    return render(req,"Blog.html")

def About(req):
    return render(req,"About.html")

def Contact(req):
    return render(req,"Contact.html")
