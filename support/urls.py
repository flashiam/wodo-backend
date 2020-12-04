from django.urls import path

from . import views

urlpatterns = [
    path('sendMessage', views.send_message, name='send'),
    path('readMessage', views.make_as_read, name='read')
]