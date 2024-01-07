from django.contrib import admin
from django.urls import path, include
from yourapp.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('', example, name='example'),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', include('yourapp.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

