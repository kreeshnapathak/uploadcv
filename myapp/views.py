from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import ResumeForm
from .models import Resume

# Create your views here.
def home(request):
    data=Resume.objects.all()
    if request.method == 'POST':
        fm = ResumeForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
        
            
    else:        
        fm = ResumeForm()
        return render(request,'myapp/home.html',{'form':fm,'data':data})


def details(request,id):
    data=Resume.objects.filter(id=id)
    
    return render(request,'myapp/details.html',{'form':data})
