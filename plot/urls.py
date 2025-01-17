from django.urls import path

from . import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path(
        "2/",
        views.Second.as_view(),
        name="second",
    ),
]
