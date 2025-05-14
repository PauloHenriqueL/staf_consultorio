from rest_framework import generics
from associado.models import Associado, Setor
from associado.serializers import AssociadoSerializer, SetorSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class AssociadoCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Associado.objects.all()
    serializer_class = AssociadoSerializer


class AssociadoRetrieveUpdateDestoyView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Associado.objects.all()
    serializer_class = AssociadoSerializer

class SetorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer


class SetorRetrieveUpdateDestoyView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer
