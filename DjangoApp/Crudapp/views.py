from django.shortcuts import render,HttpResponse


def index(req):
    data={"age":[3,5,7,8]}
    return render(req,'index.html',context=data)

def dynamic(req,id):
    return HttpResponse(id)

def about(req):
    return render(req,"about.html")