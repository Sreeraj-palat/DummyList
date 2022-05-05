from django.urls import path
from . import views

urlpatterns = [
    path('home',views.homefun,name='home'),
    path('student',views.studentfun,name='student'),
    path('viewstudent',views.viewstudentfun,name='viewstudent'),
    path('galary',views.galaryfun,name='galary'),
    

]