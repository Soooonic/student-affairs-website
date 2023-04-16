import email
from unicodedata import name
from django.shortcuts import render
from .models import Sign
# from .forms import LoginForm

# Create your views here.
def home(request):
       return render(request ,'pages/home.html')

def searchid(request):
       return render(request ,'pages/searchid.html')

def active(request):
       return render(request ,'pages/active.html' )

def status(request):
       return render(request ,'pages/status.html')

def depart(request):
       return render(request ,'pages/depart.html')              

def index(request):
  
     return render(request ,'pages/index.html', {'pro': Sign.objects.get(id ='20200458')})

def about(request):
   if request.method == "POST" :
       x = request.POST.get('Name')
       y =request .POST.get('id')
       e = request.POST.get('email')
       s = request.POST.get('status')
       l = request.POST.get('level')
       d = request.POST.get('department')
       g = request.POST.get('gpa')
       dt = request.POST.get('dateOfBirth')
       ge = request.POST.get('gender')
       p = request.POST.get('phone')
       data = Sign(name= x ,id = y , email=e , status = s , level= l , department = d , gpa =g , dateOfBirth = dt , gender = ge , phone= p)
       data.save()


   return render(request ,'pages/about.html')

   