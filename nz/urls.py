from django.urls import path
from nz.views import *
app_name="anything"
urlpatterns=[
    path('kane/',kane,name="kane"),
    path("boult/",boult,name="boult")
]