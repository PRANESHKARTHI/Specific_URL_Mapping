from django.urls import path
from sa.views import *
app_name="nothing"
urlpatterns=[
    path('abd/',abd,name="abd"),
    path("steyn/",steyn,name="steyn")
]