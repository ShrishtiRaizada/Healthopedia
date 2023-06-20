
from django.urls import path
from app import views

urlpatterns = [
    path('', views.Login, name="login"),
    path('signup/', views.SignUp, name="Signup"),
    path('home/',views.patient,name="patient"),
    path('docprofile/',views.doctor,name="doctor"),
    path('error/',views.error,name="Error"),
    path('blogpost/',views.blogpost,name="Blogpost"),
    path('allblog/',views.blogs,name="blogs"),
    path('mental/',views.mental,name="mental"),
    path('heart/',views.heart,name="heart"),
    path('covid/',views.covid,name="covid"),
    path('immune/',views.immune,name="immune"),
    path('getblog/<int:id>',views.getblog,name="getblog"),


]

