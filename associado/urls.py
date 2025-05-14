from django.urls import path
from . import views


urlpatterns = [
    path('associado', views.AssociadoCreateListView.as_view(), name='associado-list'),
    path('associado/<int:pk>', views.AssociadoRetrieveUpdateDestoyView.as_view(), name='associado-update'),
    path('setor', views.SetorCreateListView.as_view(), name='setor-list'),
    path('setor/<int:pk>', views.SetorRetrieveUpdateDestoyView.as_view(), name='setor-update'),
]