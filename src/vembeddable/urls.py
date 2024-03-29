from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('verify/<str:video_id>/', views.verify, name='verify'),
]
