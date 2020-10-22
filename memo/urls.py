from django.urls import path
from . import views

app_name = 'memo'

urlpatterns =[
    path("",views.MemoHomeView,name="homelist"),
    path("list/",views.MemoListView,name="list"),
    path("delete/",views.MemoDeleteView,name="delete"),
    path("create/",views.MemoCreateView,name="create"),
]