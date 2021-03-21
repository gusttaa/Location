from .models import Local
from .serializers import LocalSerializer
from rest_framework import viewsets

class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer