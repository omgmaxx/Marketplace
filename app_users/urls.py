from django.urls import path

from .views import RegisterUser, LogIn, LogOut, Reset, ResetConfirm, UserPrefs

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LogIn.as_view(), name='login'),
    path('logout/', LogOut.as_view(), name='logout'),
    path('reset/<uidb64>/<token>/', ResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset/', Reset.as_view(), name='reset'),
    path('prefs/', UserPrefs.as_view(), name='user_pref'),
]