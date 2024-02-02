from django.urls import path

# from blog import views
# e a mesma coisa
from . import views

urlpatterns = [
    path('', views.blog),
    path('exemple', views.exemple)
]