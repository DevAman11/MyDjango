from django.shortcuts import render


def index(req):
    data={"age":[3,5,7,8]}
    return render(req,'index.html',context=data)

def dynamic(req,id):
    return render(req,id)

def Home(req):
    return render(req,"Home.html")

def About(req):
    return render(req,"About.html")

def Loan(req):
    return render(req,"Loan.html")

def Card(req):
    return render(req,"Card.html")

def Privacy(req):
    return render(req,"Privacy.html")

def Contact(req):
    return render(req,"Contact.html")
