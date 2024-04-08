"""CollegeEventManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

from college import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    
    path('adminlogin', LoginView.as_view(template_name='college/adminlogin.html'),name='adminlogin'),
    path('studentlogin', LoginView.as_view(template_name='college/studentlogin.html'),name='studentlogin'),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='college/index.html'),name='logout'),
    path('admin-home', views.admin_home_view,name='admin-home'),
    path('student-home', views.student_home_view,name='student-home'),
    path('studentsignup', views.student_signup_view,name='studentsignup'),
    
    path('admin-events', views.admin_events_view,name='admin-events'),
    path('admin-aboutus', views.admin_aboutus_view,name='admin-aboutus'),
    path('admin-contactus', views.admin_contactus_view,name='admin-contactus'),
    path('admin-add-event', views.admin_add_event_view,name='admin-add-event'),
    path('student-events', views.student_events_view,name='student-events'),
    path('student-aboutus', views.student_aboutus_view,name='student-aboutus'),
    path('student-contactus', views.student_contactus_view,name='student-contactus'),
   
]
