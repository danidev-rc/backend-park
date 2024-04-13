from rest_framework import serializers
from preinscription.models import Preinscription

class PreinscriptionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Preinscription
    fields = '__all__'