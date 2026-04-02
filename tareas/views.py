from rest_framework import viewsets, permissions, generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from .models import Tarea
from .serializers import TareaSerializer, RegistroSerializer

class TareaViewSet(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["completada"]
    search_fields = ["titulo", "descripcion"]
    ordering_fields = ["creada", "titulo"]
    ordering = ["-creada"]

    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class RegistroView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistroSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "username": user.username})