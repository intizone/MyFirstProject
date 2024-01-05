from django.contrib import admin
from django.urls import path, include
from yourapp.views import *

urlpatterns = [
    # path('', example, name='example'),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('main/', include('yourapp.urls'))
]