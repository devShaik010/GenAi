from django.urls import path
from .views import index,new
urlpatterns = [
    path('',index ),
    path('new',new)
    
]
