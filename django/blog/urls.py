from . import views
from django.urls import path

urlpatterns = [
    path('home', views.PageList.as_view(), name='home'),
    path('<slug:slug>/', views.PageDetail.as_view(), name='page_detail'),
]