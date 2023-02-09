
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('badwinshop.urls')),
    path('credentials/', include('credentials.urls')),
]
