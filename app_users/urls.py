from django.urls import path

from views import RegisterUser, LogIn, LogOut, EditUser

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('edit/', EditUser.as_view(), name='edit-user'),
    path('login/', LogIn.as_view(), name='login'),
    path('logout/', LogOut.as_view(), name='logout'),
]