from django.urls import path
from instamart.views import *

app_name='instamart'

urlpatterns = [
    path('', instamart, name='instamart'),
]
