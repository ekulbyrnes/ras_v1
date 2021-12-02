from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.PageList.as_view(), name='list'),
    path('<slug:slug>/', views.PageDetail.as_view(), name='page_detail'),
]