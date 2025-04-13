from rest_framework import viewsets
from .models import Labs
from .serializers import LabsSerializer

class LabsViewSet(viewsets.ModelViewSet):
    queryset = Labs.objects.all()
    serializer_class = LabsSerializer
