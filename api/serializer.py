from rest_framework import fields, serializers
from .models import pizza, toppings, size, toppings
# from api.models2 i2mport 

class pizza_serialization(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pizza
        fields  = '__all__'