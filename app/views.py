from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from app.models import Signup
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
@login_required(login_url='/')
def SignUp(request):
    error=""
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name  = request.POST.get('last_name')
        email      = request.POST.get('email')
        username      = request.POST.get('username')
        address    = request.POST.get('address')
        city       = request.POST.get('city')
        state      = request.POST.get('state')
        pincode    = request.POST.get('pincode')
        signup_as=  request.POST.getlist('signup_as', None)
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if(password1!=password2):
            error="Your password and confirm password are not Same!!"
        elif (len(first_name)==0 or len(last_name)==0  or len(email)==0  or len(username) ==0 or len(address)==0  or len(city)==0  or len(state)==0
             or len(pincode)==0  or len(password1)==0  or len(password2)==0 ):
            error="Please Fill all the fields"
        elif  Signup.objects.filter(username=username).exists() :
                error="Username already taken please take another username"

        if (len(error) > 0):
            etext = {'error': error}
            return render(request, 'error.html', etext)
        else:
            my_user = Signup.objects.create(first_name=first_name, last_name=last_name, email=email, username=username,
                                            address=address
                                            , city=city, state=state, pincode=pincode, signup_as=signup_as,
                                            password1=password1)
            my_user.save()
            print(my_user)
            user = User.objects.create_user(username, email, password1)
            user.save()
            return redirect('/')




    return render(request, 'Signup.html')


def Login(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password = request.POST.get('password')
        login_as=request.POST.get('login_as')
       # if(len(username)==0 or len(password)==0):
           # return HttpResponse("Please fill all the fields")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if(login_as=="Patient"):
                patient_details=Signup.objects.get(username=username)
                context={'patient_details':patient_details}
                print(context)
                return render(request,'Patient.html',context)
            elif(login_as=="Doctor"):
                doctor_details = Signup.objects.get(username=username)
                context = {'doctor_details': doctor_details}
                return render(request, 'Doctor.html', context)


        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')


def patient(request):
    return render(request, 'Patient.html')

def doctor(request):
    return render(request, 'Doctor.html')

def error(request):
    return render(request,'error.html')