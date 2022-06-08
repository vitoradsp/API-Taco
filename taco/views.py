from rest_framework import mixins, permissions, viewsets
from rest_framework.response import Response
from taco.models import Alimento
from taco.serializers import AlimentoSerializer
import sqlite3

class AlimentoViewSet(viewsets.ModelViewSet):
    queryset = Alimento.objects.all()
    serializer_class = AlimentoSerializer
    
