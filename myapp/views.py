from django.shortcuts import render,redirect
from myapp.models import school,personalschool
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login  ,logout

# Create your views here.

def register(request):
    if request.method=='POST':
        if request.POST.get('register')=='register':
            name=request.POST.get('username')
            name1=request.POST.get('password')

            if User.objects.filter(username=name).exists():
                return redirect('register')
            
            User.objects.create_user(username=name,password=name1)
            return redirect('login')
        
    return render(request,'register.html')

def loginn(request):
    if request.method=='POST':
        if request.POST.get('login')=='login':
              name=request.POST.get('username')
              name1=request.POST.get('password')

              if  not User.objects.filter(username=name):
                  return redirect('login')
              
              userdetails=authenticate(request,username=name,password=name1)

              if userdetails is None:
                  return redirect('login')
              else:
                  login(request,userdetails)
                  return redirect('index')
              
    return render(request,'login.html')


def logoutt(request):
    if request.method=='POST':
        if request.POST.get('logout')=='logout':
            logout(request)

    return redirect('register')



@login_required(login_url='register')
def show(request):
    new=personalschool.objects.filter(user=request.user)

    if request.method=='POST':
        if request.POST.get('add')=='add':
            name=request.POST.get('name')
            te_name=request.POST.get('teacher')
            sub_name=request.POST.get('subject')
            number=request.POST.get('number')
            personalschool.objects.create(user=request.user,student_name=name,teacher_name=te_name,subject=sub_name,number=number)
         
        if request.POST.get('search')=='search':
            name=request.POST.get('name')
            new= personalschool.objects.filter(user=request.user,student_name__icontains=name)
        

    return render(request,'index.html',{'st':new})

@login_required(login_url='register')
def new(request,id):
    if request.method=='POST':
        if request.POST.get('update')=='update':
            name=request.POST.get('name')
            te_name=request.POST.get('teacher')
            sub_name=request.POST.get('subject')
            number=request.POST.get('number')
            personalschool.objects.filter(id=id).update(student_name=name,teacher_name=te_name,subject=sub_name,number=number)
            return redirect('index')
        
    new=personalschool.objects.filter(id=id).get()
    return render(request,'update.html',{'st':new})

@login_required(login_url='register')
def deletee(request,id):
    if request.method=='POST':
        if request.POST.get('delete')=='delete':
            personalschool.objects.filter(id=id).delete()
    
    return redirect('index')

def about(request):
    return render(request,'about.html')