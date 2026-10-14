from django.urls import path
from stdmanageapp import views

urlpatterns=[
    path("dashboard/",views.home,name="home"),
    path("register/",views.signUp,name="register"),
    path("",views.signIn,name="login")

]