from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addItem', views.add_item, name='addItem')
]