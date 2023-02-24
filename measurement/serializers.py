from rest_framework import serializers

from measurement.models import Sensor, Measurment


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurment
        fields = ['temperature', 'created_at', 'photo']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurmentSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
