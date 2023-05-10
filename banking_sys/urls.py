
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('', include('home.urls')),
    path('customers/', include('customers.urls')),
    path('transfer/', include('transfer.urls')),
    path('admin/', admin.site.urls),
]
