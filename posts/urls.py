from django.urls import path
from .views import *
from django.utils import timezone

app_name = "posts"

urlpatterns = [
    path("recent_postlist/",recent_postlist,name="recent_postlist"),
    path("makepost/",makepost,name="makepost"),
    path("<str:id>",detail,name="detail"),
    path("create/",create, name="create"),
    path('edit/<str:id>', edit, name="edit"),
]