from rest_framework import serializers
from associado.models import Associado


class AssociadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Associado
        fields = '__all__'
