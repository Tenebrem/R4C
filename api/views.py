from rest_framework.generics import CreateAPIView
from .serializers import RobotSerializer


class RobotCreateView(CreateAPIView):
    serializer_class = RobotSerializer
