"""
URL configuration for MyProject project.
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from yourapp.views import *

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('main/', include('yourapp.urls')),

    path('viewportfolios/', view_portfolio, name='view_portfolio'),
    path('viewmessages/', view_messages, name='view_messages'),
    path('viewteams/', view_teams, name='view_teams'),

    path('updateteams/', update_team, name='update_team'),
    path('updatemessages/', update_message, name='update_message'),
    path('updateportfolios/', update_portfolio, name='update_portfolio'),

    path('deletemessages/', delete_message, name='delete_message'),
    path('deleteteams/', delete_team, name='delete_team'),
    path('deleteportfolios/', delete_portfolio, name='delete_portfolio'),

    path('createportfolios/', create_portfolio, name='create_portfolio'),
    path('createmessages/', create_message, name='create_message'),
    path('createteams/', create_team, name='create_team'),
]