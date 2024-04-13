from django.urls import path
from . import views
# from .views import 

app_name = 'api'

urlpatterns = [
  path('preinscriptions/', views.PreinscriptionListCreate.as_view(), name='preinscription-list-create'),
  path('preinscriptions/<int:pk>/', views.PreinscriptionDetail.as_view(), name='preinscription-detail'),
]
