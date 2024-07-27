from django.shortcuts import render,HttpResponse
from myapp.models import contact_view
from .forms import coderform
from myapp.models import register_view
from .forms import coderregister
# Create your views here.

def index(request):
    return render(request,"home.html")

def contact(request):
    if request.method =="POST":
        fm = coderform(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ms = fm.cleaned_data['message']
            
            data1 = contact_view(name = nm,email =em,message = ms)
            data1.save()
            print("data is stored into table")
    else:
        fm = coderform()
        
    return render(request,'contact.html',{'form':fm})

def register(request):
    if request.method =="POST":
        fmr = coderregister(request.POST)
        if fmr.is_valid():
            nm = fmr.cleaned_data['name']
            em = fmr.cleaned_data['email']
            st = fmr.cleaned_data['state']
            ct = fmr.cleaned_data['city']
            zp = fmr.cleaned_data['zipcode']
            sg = fmr.cleaned_data['suggestions']
            
            data2 = register_view(name = nm,email =em, state=st,city = ct,zipcode=zp,suggestions = sg)
            data2.save()
            print("data is stored into table")
    else:
        fmr = coderregister()
        
    return render(request,'forms.html',{'form':fmr})

# def index(request):
#     return render(request,"index.html")

def about(request):
    return render(request,"Explore.html")

def home(request):
    return render(request,"home.html")