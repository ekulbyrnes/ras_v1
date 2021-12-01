from . import views
from django.urls import path

urlpatters = [
    path('', views.PageList.as_view(), name='home'),
    path('<slug:slug>/', views.PageDetail.as_view(), name='page_detail'),
]