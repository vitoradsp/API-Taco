from rest_framework import viewsets
from taco.models import Alimento
from taco.serializers import AlimentoSerializer


class AlimentoViewSet(viewsets.ModelViewSet):
    queryset = Alimento.objects.all()
    serializer_class = AlimentoSerializer
    
