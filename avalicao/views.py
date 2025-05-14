from rest_framework import generics
from avalicao.models import Avaliacao, Avaliado, Avaliador
from avalicao.serializers import AvaliacaoSerializer, AvaliadoSerializer, AvaliadorSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class AvaliacaoCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

class AvaliacaoRetrieveUpdateDestoyView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

class AvaliadoCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Avaliado.objects.all()
    serializer_class = AvaliadoSerializer

class AvaliadoRetrieveUpdateDestoyView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Avaliado.objects.all()
    serializer_class = AvaliadoSerializer

class AvaliadorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Avaliador.objects.all()
    serializer_class = AvaliadorSerializer

class AvaliadorRetrieveUpdateDestoyView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Avaliador.objects.all()
    serializer_class = AvaliadorSerializer