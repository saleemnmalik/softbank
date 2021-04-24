from django.urls import path
from . import views





urlpatterns =[
    path("postdata", views.DataUsingClass.as_view()),
    path("updatedata", views.DataUpdate.as_view()),
    path("deletedata", views.DataDelete.as_view()),

]