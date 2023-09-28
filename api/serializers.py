from rest_framework import serializers
from robots.models import Robot


class RobotSerializer(serializers.ModelSerializer):
    serial = serializers.CharField(read_only=True)

    def create(self, validated_data):
        robot_model = validated_data.get('model')
        robot_version = validated_data.get('version')

        robot_serial = f'{robot_model}-{robot_version}'

        validated_data['serial'] = robot_serial

        robot = Robot(**validated_data)
        robot.save()
        return robot

    class Meta:
        model = Robot
        fields = '__all__'
