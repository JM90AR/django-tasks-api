from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import TareaViewSet, RegistroView

router = DefaultRouter()
router.register("tareas", TareaViewSet, basename="tarea")

urlpatterns = router.urls + [
    path("registro/", RegistroView.as_view()),
]