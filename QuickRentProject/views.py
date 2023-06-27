from django.http import HttpResponse
from django.shortcuts import render,redirect
from carinfo.models import carinfo
from usersdata.models import userdata
from django.contrib.messages import middleware
import qrcode as qr


def home(request):
    if request.method == 'GET':
            message = request.GET.get('message')
            print(message)
    return render(request,"DE_main.html", {'message' : message})

def login(request):
    message = None
    try:
        if request.method == 'GET':
            message = request.GET.get('message')
            print(message)

        if request.method == 'POST': 
            email = request.POST.get('email')
            paswd=request.POST.get('paswd')
            check = userdata.objects.get(email=email,password=paswd)
            if check is not None:
                return redirect("/home")
    except:
        pass
    return render(request,"DE_login.html" , {'message' : message})

def signUp(request):
    try:
        if request.method == 'POST':
            userName = request.POST.get('name')
            email = request.POST.get('email')
            pass1=request.POST.get('pass1')
            pass2=request.POST.get('pass2')
            if pass1 == pass2:
                print('')
                try:
                    myUser = userdata.objects.create(userName= userName, email=email , password=pass1)
                    url = "/?message=success"
                    return redirect(url)
                except:
                    pass
    except:
        pass
    return render(request,"DE_signup.html")

def aboutUs(request):
    return render(request,"DE_aboutUs.html")

def contact(request):
    return render(request,"DE_contact.html")

def carDetail(request):
    data={}
    try:
        n1=request.POST.get('trip-start').split('-')
        n2=request.POST.get('trip-end').split('-')
        try:
            it = request.POST.get('location')
            year = (int(n2[0]) - int(n1[0]))*8760
            month= (int(n2[1]) - int(n1[1]))*720
            day = (int(n2[2]) - int(n1[2]))*24
            totalHrs=(year+month+day)
            print(totalHrs , it)
            carData = carinfo.objects.filter(location__icontains=it)
            data={
                "carData":carData,
                "totalHrs":totalHrs,  
                "location":it
            } 
        except:
            pass
        print(n2+n1)
    except:
        pass
    return render(request, "carDetail.html",data)
   
def moreInfo(request):
    data={}
    try:
        carId = int(request.POST.get('n1'))
        totalHrs = int(request.POST.get('n2'))
        carData = carinfo.objects.get(id=carId)
        tripFare=int(carData.carRent)*totalHrs
        damageProtection = totalHrs*20;
        totalRent=tripFare+damageProtection+100
        data={
                "carData":carData,
                "damageProtection":damageProtection,
                "totalRent":totalRent,
                "tripFare":tripFare,
            }
        print(carId , totalHrs,totalRent )
    except:
        pass
    return render(request, "moreInfo.html",data)