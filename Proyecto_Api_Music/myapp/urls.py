from django.urls import path
from .views import VictrolaView, WaitListView

urlpatterns = [
    path('music/', VictrolaView.as_view(), name='music_list'),
    path('music/<int:id>/', VictrolaView.as_view(), name='music_process'),
    path('waitlist/', WaitListView.as_view(), name='wait_list'),
    path('waitlist/<int:id>/', WaitListView.as_view(), name='wait_process')

]
