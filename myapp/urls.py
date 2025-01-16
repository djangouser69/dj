from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test/", views.test, name="test"),
    path("class/", views.About.as_view()),
    path("stuff/", views.stuff, name="stuff"),
    path("plot/", views.plot, name="plot"),
    path("gh/", views.Gh.as_view(), name="gh"),
    path("new/", views.newview, name="new"),
]
