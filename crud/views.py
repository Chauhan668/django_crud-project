from django.shortcuts import render , HttpResponseRedirect
from . models import User
from .forms import StudentRegisteration
# Create your views here.
def addandshow(request):
    if request.method =='POST':
        fm = StudentRegisteration(request.POST)
        if fm.is_valid(): 
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ps = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=ps)
            reg.save()
            fm = StudentRegisteration()
    else: 
            fm = StudentRegisteration()
    std = User.objects.all()        
    return render(request,'crud/addandshow.html',{'form':fm ,'stud':std})


    # This fucntion will delete items

def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


# This functionn will update and edit.
def update_data(request ,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegisteration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegisteration(instance=pi)
    return render(request, 'crud/updatestudent.html',{'form': fm})



