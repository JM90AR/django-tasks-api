from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ["id", "titulo", "descripcion", "completada", "creada", "usuario"]
        read_only_fields = ["id", "creada", "usuario"]

class RegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email", ""),
            password=validated_data["password"],
        )
        return user