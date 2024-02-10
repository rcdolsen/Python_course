from django.urls import path

# from blog import views
# e a mesma coisa
from . import views

app_name = 'blog'

# blog/
# Django URLs:
# https://docs.djangoproject.com/en/5.0/topics/http/urls/
urlpatterns = [
    path('post/<int:post_id>/', views.post, name='post'),
    path('', views.blog, name='home'),
    path('exemple/', views.exemple, name='exemple')
]
