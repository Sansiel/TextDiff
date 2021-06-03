from django.contrib import admin
from django.urls import path, include


# Короч, тут ничего важного. Иди в main
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
]
