from django.urls import path
from . import views

app_name = 'memo'

urlpatterns =[
    path("",views.MemoListView.as_view(),name="list"),
    path("<int:pk>/",views.MemoDetailView.as_view(), name="detail"),
]