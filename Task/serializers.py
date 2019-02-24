from Task.models import MissouriData
from rest_framework import serializers


class MissouriNonIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissouriData
        exclude = ('id',)


class MissouriSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissouriData
        fields = '__all__'
