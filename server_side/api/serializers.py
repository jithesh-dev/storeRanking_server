from rest_framework import serializers
from .models import Store


class StoreSerializer(serializers.ModelSerializer):
    rank = serializers.IntegerField()

    class Meta:
        model = Store
        fields = "__all__"
