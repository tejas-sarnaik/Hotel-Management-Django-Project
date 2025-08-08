from django.shortcuts import render,redirect

from peoplemanagement.models import People

# Create your views here.
def home(request):
    return render(request,'peoplemanagement/home.html')

def aboutus(request):
    return render(request,'peoplemanagement/aboutus.html')

def record(request):
    data=People.objects.all()
    context={
        "data":data
    }

    return render(request,'peoplemanagement/record.html',context)

def registration(request):
    if request.method == 'POST':
        n=request.POST.get("name")
        e=request.POST.get("email")
        m=request.POST.get("mbl")
        ci=request.POST.get("checkin")
        co=request.POST.get("checkout")
        gu=request.POST.get("guests")
        ro=request.POST.get("roomtype")
        it=request.POST.get("identitytype")
        ip=request.POST.get("identityproof")
        data=People(name=n,email=e,mbl=m,checkin=ci,checkout=co,guests=gu,roomtype=ro,identitytype=it,identityproof=ip)
        data.save()

    return render(request,'peoplemanagement/registration.html')

def update(request,id):
    data=People.objects.get(id=id)
    context={
        'data':data
    }
    if request.method == 'POST':
        n=request.POST.get("name")
        e=request.POST.get("email")
        m=request.POST.get("mbl")
        ci=request.POST.get("checkin")
        co=request.POST.get("checkout")
        gu=request.POST.get("guests")
        ro=request.POST.get("roomtype")
        it=request.POST.get("identitytype")
        ip=request.POST.get("identityproof")
        data.name=n
        data.email=e
        data.mbl=m
        data.checkin=ci
        data.checkout=co
        data.guests=gu
        data.roomtype=ro
        data.identitytype=it
        data.identityproof=ip
        data.save()
        return redirect('/record/')
        
    return render(request,'peoplemanagement/update.html',context )

def delete(request,id):
    data=People.objects.get(id=id)
    data.delete()
    return redirect('/record/')



