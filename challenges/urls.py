from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="index"), # /challenges/
	path("<int:month>", views.mounthly_challenge_by_number),
	path("<str:month>", views.mounthly_challenge, name="month-challenge")
]