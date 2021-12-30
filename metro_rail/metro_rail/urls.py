
from django.contrib import admin
from django.urls import path,include
from metro_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('metro_app.urls')),
 
    
]

