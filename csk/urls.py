from django.urls import path
from csk.views import *

app_name = "something"

urlpatterns = [
    path("csk/",csk,name="csk")
]