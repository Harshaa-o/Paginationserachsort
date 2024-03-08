from django.urls import path
from . import views


app_name = 'pssapp'
urlpatterns = [ 
   
    path('added/', views.sublist, name='sublist'),
    
    path('subject_list/', views.subject_list, name='subject-list'),
    path('search/', views.subject_search, name='subject-search'),
    

]
