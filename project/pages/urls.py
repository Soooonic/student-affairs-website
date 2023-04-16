from django.urls import  path
from . import views

urlpatterns = [
    path('',views.index , name='index'),
    path('about',views.about , name='about'),
    path('home',views.home , name='home'),
    path('search',views.searchid , name='searchid'),
    path('active',views.active , name='active'),
    path('status',views.status , name='status'),
    path('depart',views.depart , name='depart'),
]