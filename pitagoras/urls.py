
from django.contrib import admin
from django.urls import path, include
import sys

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calc_app.urls'))
]