from django.urls import path
from . import views


urlpatterns = [
    path('avaliacao', views.AvaliacaoCreateListView.as_view(), name='avaliacao-list'),
    path('avaliacao/<int:pk>', views.AvaliacaoRetrieveUpdateDestoyView.as_view(), name='avaliacao-update'),
]