from rest_framework import serializers
from avalicao.models import Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Avaliacao
        fields = '__all__'
