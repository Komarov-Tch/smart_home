from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurment
from measurement.serializers import SensorSerializer, MeasurmentSerializer, SensorDetailSerializer


class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurmentView(CreateAPIView):
    queryset = Measurment.objects.all()
    serializer_class = MeasurmentSerializer

    def post(self, request, *args, **kwargs):
        temperature = request.data.get('temperature')
        sensor = request.data.get('sensor')
        if sensor is None or temperature is None:
            return Response({'error': 'ошибка в датчике температуры'})
        sensor = Sensor.objects.get(id=request.data.get('sensor'))
        params = {'temperature': request.data.get('temperarure'),
                  'sensor': sensor,
                  'photo': request.data.get('photo'),
                  }
        meterik = Measurment.objects.create(**params)
        result = {'sensor': meterik.sensor.id,
                  'temperature': meterik.temperature,
                  'created_at': meterik.created_at}
        return Response(result)


class SensorDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer