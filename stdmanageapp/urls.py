from django.urls import path
from stdmanageapp import views

urlpatterns=[
    path("dashboard/",views.home,name="home"),
    path("register/",views.signUp,name="register"),
    path("logout/",views.signOut,name="logout"),
    path("all-course/",views.courseList,name="all_course"),
    path("",views.signIn,name="login")

]