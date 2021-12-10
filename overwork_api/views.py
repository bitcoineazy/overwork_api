from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import OverworkSerializer


class OverworkViewSet(viewsets.ViewSet):
    @action(url_path='burnout', methods=['POST'], detail=False)
    def overwork_test(self, request):
        serializer = OverworkSerializer(data=request.data)
        if serializer.is_valid():
            day = serializer.validated_data['day']
            month = serializer.validated_data['month']
            year = serializer.validated_data['year']
            sex = serializer.validated_data['sex']
            first_value = int(serializer.validated_data['first_value'])
            second_value = int(serializer.validated_data['second_value'])
            if 0 < second_value - first_value <= 12:
                return Response({'Введенные значения соответствуют отсутствию переутомления.'})
            if 12 < second_value - first_value <= 16:
                return Response({'Введенные значения соответствуют небольшому переутомлению. Рекомендуется снижение нагрузки.'})
            if 16 < second_value - first_value <= 22:
                return Response({'Введенные значения соответствуют высокому уровню переутомления. Рекомендуется снижение нагрузки или отпуск.'})
            if 22 < second_value - first_value:
                return Response({'Error'})
        else:
            return Response(serializer.errors)

