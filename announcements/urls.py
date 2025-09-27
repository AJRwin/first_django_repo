from django.urls import path
from core import views  # use views from core

app_name = "announcements"

urlpatterns = [
    path("", views.announcement_list, name="list"),
    path("<int:id>/", views.announcement_detail, name="detail"),
]
