from ind.views import *
from django.urls import path
app_name="some_thing"

urlpatterns=[
    path("msd/",msd,name="msd"),
    path("virat/",virat,name="virat")
]