from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('create', views.create, name='create'),
    path('/<str:pk>', views.go, name='go')
]
    