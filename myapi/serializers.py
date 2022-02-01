from rest_framework import serializers

from .models import Vehicles

class VehiclesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicles
        fields = ('car_id', 'make', 'model', 'avg_rating')
class POSTCarsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicles
        fields = ('make', 'model')
class POSTCarsRateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicles
        fields = ('car_id', 'rating')

    #def validate(self, data):
        #auction = Vehicles.objects.get(data=data['car_id'])
        #amount = data.get('rates_number')
        #amount+=1
        #print(amount)
        #if not amount:
            #msg = {'amount': ['this field is not valid']}
            #raise serializers.ValidationError(msg)

class GETCarsPopularSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicles
        fields = ('car_id', 'make', 'model',  'rates_number')
