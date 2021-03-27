from rest_framework import viewsets
from .serializer import pizza_serialization
from .models import pizza

# Create your views here.


class piza_viewset(viewsets.ModelViewSet):
    queryset =pizza.objects.all()
    serializer_class = pizza_serialization
