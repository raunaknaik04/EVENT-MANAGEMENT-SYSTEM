from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,reverse

from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from college import models
from . import forms,models
# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'college/index.html')


def aboutus_view(request):
    return render(request,'college/aboutus.html')


def is_student(user):
    return user.groups.filter(name='STUDENT').exists()


def afterlogin_view(request):
    if is_student(request.user):
        return redirect('student-home')
    else:
        return redirect('admin-home')

#============================================================================================
# ADMIN RELATED views start
#============================================================================================

@login_required(login_url='adminlogin')
def admin_home_view(request):
    return render(request,'college/admin_home.html')

@login_required(login_url='adminlogin')
def admin_events_view(request):
    
    events=models.Event.objects.all()
    return render(request,'college/admin_event.html',{'events':events})

@login_required(login_url='adminlogin')
def admin_aboutus_view(request):
    return render(request,'college/admin_aboutus.html')

@login_required(login_url='adminlogin')
def admin_contactus_view(request):
    return render(request,'college/admin_contactus.html')



@login_required(login_url='adminlogin')
def admin_add_event_view(request):
    eventForm=forms.EventForm()
    mydict={'eventForm':eventForm}
    if request.method=='POST':
        eventForm=forms.EventForm(request.POST,request.FILES)
        if eventForm.is_valid():
            eventForm.save()
        return HttpResponseRedirect('/admin-events')
    return render(request,'college/regevent.html',context=mydict)

#============================================================================================
# STUDENT RELATED views start
#============================================================================================
@login_required(login_url='studentlogin')
def student_home_view(request):
    return render(request,'college/student_home.html')


def student_signup_view(request):
    userForm=forms.StudentUserForm()
    mydict={'userForm':userForm,}
    if request.method=='POST':
        userForm=forms.StudentUserForm(request.POST)
        if userForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            my_group = Group.objects.get_or_create(name='STUDENT')
            my_group[0].user_set.add(user)
        return HttpResponseRedirect('studentlogin')
    return render(request,'college/student_signup.html',context=mydict)


@login_required(login_url='studentlogin')
def student_events_view(request):
    events=models.Event.objects.all()
    return render(request,'college/student_event.html',{'events':events})

@login_required(login_url='studentlogin')
def student_aboutus_view(request):
    return render(request,'college/student_aboutus.html')

@login_required(login_url='studentlogin')
def student_contactus_view(request):
    return render(request,'college/student_contactus.html')
