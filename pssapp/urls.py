from django.urls import path
from . import views


app_name = 'pssapp'
urlpatterns = [ 
   
    
    
    path('subject_list/', views.subject_list, name='subject-list'),
    
    

]
