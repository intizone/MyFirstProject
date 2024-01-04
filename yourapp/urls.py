from django.urls import path
from .views import *

urlpatterns = [
    path("main", home),
    path("main", lambda a:a),
]