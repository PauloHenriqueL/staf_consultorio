from django.urls import path
from . import views


urlpatterns = [
    path('avaliacao', views.AvaliacaoCreateListView.as_view(), name='avaliacao-list'),
    path('avaliacao/<int:pk>', views.AvaliacaoRetrieveUpdateDestoyView.as_view(), name='avaliacao-update'),
    path('avaliado', views.AvaliadoCreateListView.as_view(), name='avaliado-list'),
    path('avaliado/<int:pk>', views.AvaliadoRetrieveUpdateDestoyView.as_view(), name='avaliado-update'),
    path('avaliador', views.AvaliadorCreateListView.as_view(), name='avaliador-list'),
    path('avaliador/<int:pk>', views.AvaliadorRetrieveUpdateDestoyView.as_view(), name='avaliador-update'),
]