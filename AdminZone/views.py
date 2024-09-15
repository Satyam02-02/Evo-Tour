from django.http import HttpResponse
from django.shortcuts import render
from general.models import ContactModel
# Create your views here.
def dashboard(request):
    if request.session.has_key("aid"):
        return render(request,"AdminZone/dashboard.html")
    else:
        return HttpResponse("<script>alert(' OHH First LogIn');window.location.href='/logIn/'</script>")
def contactmgmt(request):
    if request.session.has_key("aid"):
        data=ContactModel.objects.all()
        return render(request,"AdminZone/contactmgmt.html",{"data":data})
    return HttpResponse("<script>alert(' OHH First LogIn');window.location.href='/logIn/'</script>")
def changepass(request):
    if request.session.has_key("aid"):
        return render(request,"AdminZone/changepass.html")
    return HttpResponse("<script>alert(' OHH First LogIn');window.location.href='/logIn/'</script>")
def logout(request):
    del request.session["aid"]
    return HttpResponse("<script>window.location.href='/logIn/'</script>")

def feedbackmgmt(request):
    if request.session.has_key("aid"):
        return render(request,"AdminZone/feedbackmgmt.html")
    return HttpResponse("<script>alert(' OHH First LogIn');window.location.href='/logIn/'</script>")
def bookingmgmt(request):
    if request.session.has_key("aid"):
        return render(request,"AdminZone/bookingmgmt.html")
    return HttpResponse("<script>alert(' OHH First LogIn');window.location.href='/logIn/'</script>")
def delData(request,id):
    data=ContactModel.objects.get(id=id)
    data.delete()
    return HttpResponse("<script>alert('Record Deleted');window.location.href='/contactmgmt/'<script>")

