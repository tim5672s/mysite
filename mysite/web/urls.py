from .views import member_view
from django.urls import path
from . import views

app_name = 'web'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('member/', views.member_view, name='member'),
    path('logout/', views.logout_view, name='logout'),
]
