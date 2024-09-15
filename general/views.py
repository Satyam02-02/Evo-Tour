from django.shortcuts import render,HttpResponse
from general import *
from general.models import ContactModel,LoginModel


# Create your views here.
def index(request):
    return render(request, "index.html")
def pre(request):
    return render(request, "home.html")
def aboutus(request):
    return render(request, "aboutUs.html")
def logIn(request):
    return render(request, "logIn.html")
def visa(request):
    return render(request, "visa.html")
def contacts(request):
    return render(request,"contacts.html")
def services(request):
    return render(request,"services.html")

def bus(request):
    return render(request,"bus.html")
def train(request):
    return render(request,"train.html")
def flight(request):
    return render(request,"flight.html")
def feedback(request):
    return render(request,"feedback.html")
def booking(request):
    return render(request,"booking.html")
def SaveData(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        mob=request.POST['mob']
        query=request.POST['query']
        data=ContactModel(name=name,email=email,mobile=mob,queue=query)
        data.save()
        return HttpResponse("<script>alert('Thanks Data Saved Successfully');window.location.href='/contacts'</script>")
    else:
        return HttpResponse("<script>alert('OHH Something Went Wrong');window.location.href='/contacts'</script>")



def loginData(request):
 try:
    if request.method == 'POST':
        aid=request.POST['aid']
        passwd=request.POST['passwd']
        lg=LoginModel.objects.get(aid=aid)
        if lg.aid==aid and lg.passwd==passwd:
            request.session['aid']=aid
            return HttpResponse("<script>alert('Logged In');window.location.href='/dashboard/'</script>")
        else:
            return HttpResponse("<script>alert('Invalid UserId or Password');window.location.href='/logIn/'</script>")
 except LoginModel.DoesNotExist:
     return HttpResponse("<script>alert('Invalid UserId or Password');window.location.href='/logIn/'</script>")
