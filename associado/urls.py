from django.urls import path
from . import views


urlpatterns = [
    path('associado', views.AssociadoCreateListView.as_view(), name='associado-list'),
    path('associado/<int:pk>', views.AssociadoRetrieveUpdateDestoyView.as_view(), name='associado-update'),
]