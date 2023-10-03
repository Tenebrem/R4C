from django.urls import path

from .views import RobotCreateView

app_name = 'api'


urlpatterns = [
    path('create_robot/', RobotCreateView.as_view(), name='create_robot'),
]
