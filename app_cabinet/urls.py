from django.urls import path

from .views import Cabinet, Profile, HistoryList, HistoryDetail

urlpatterns = [
    path('', Cabinet.as_view(), name='cabinet'),
    path('profile/', Profile.as_view(), name='profile'),
    path('purchases/', HistoryList.as_view(), name='history'),
    path('purchases/<int:pk>', HistoryDetail.as_view(), name='history-item'),
]
