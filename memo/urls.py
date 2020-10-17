from django.urls import path
from . import views

app_name = 'memo'

urlpatterns =[
    path("",views.MemoHomeView,name="homelist"),
    path("list/",views.MemoListView.as_view(),name="list"),
    # path("<int:pk>/",views.MemoDetailView.as_view(), name="detail"),
    # path("",views.MemoCreateView.as_view(), name="create"),
    # path("<int:pk>/update/",views.MemoUpdateView.as_view(), name="update"),
]