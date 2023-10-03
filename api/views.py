from rest_framework.generics import CreateAPIView

from .serializers import RobotSerializer


class RobotCreateView(CreateAPIView):
    """ Вьюсет создания робота"""
    serializer_class = RobotSerializer
