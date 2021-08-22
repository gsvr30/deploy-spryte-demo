from django.urls import path
from . import views

app_name = 'dob'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    path('', views.index, name='index'),
    path('welcome/', views.hello, name='welcome'),
]
