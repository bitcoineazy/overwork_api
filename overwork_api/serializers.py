from rest_framework import serializers


class OverworkSerializer(serializers.Serializer):
    day = serializers.IntegerField()
    month = serializers.IntegerField()
    year = serializers.IntegerField()
    sex = serializers.IntegerField()
    first_value = serializers.IntegerField()
    second_value = serializers.IntegerField()
