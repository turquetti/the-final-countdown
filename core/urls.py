from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ca/', include('ca.urls')),
    path('admin/', admin.site.urls),
]
