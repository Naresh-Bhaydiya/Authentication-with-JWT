from django.urls import path
from . import views

urlpatterns = [
    path('signupAPI/',views.signupAPI.as_view(),name='signup'),
    path('loginAPI/',views.loginAPI.as_view(),name='loginAPI'),
    path('BookAPI/',views.BookAPI.as_view(),name='BookAPI'),

]