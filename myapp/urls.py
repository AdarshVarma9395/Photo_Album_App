from django.urls import path
from . views import *

urlpatterns = [
    path("", gallery , name='gallery'),
    path("photo/<str:pk>/", viewphoto , name='photo'),
    path("add/", addphoto , name='add'),
]