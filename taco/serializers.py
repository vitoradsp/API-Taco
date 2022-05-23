from rest_framework import serializers

from taco.models import Alimento


class AlimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimento
        fields = 'name','kcal', 'protein', 'fat', 'carbo'


