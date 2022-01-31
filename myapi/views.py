from django.shortcuts import render
from rest_framework import viewsets
from .serializers import VehiclesSerializer,POSTCarsSerializer,POSTCarsRateSerializer,GETCarsPopularSerializer
from .models import Vehicles
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from .get_models import get_models
from rest_framework.decorators import api_view
# Create your views here.


class VehiclesViewSet(viewsets.ModelViewSet):
    queryset = Vehicles.objects.all().order_by('car_id')
    serializer_class = VehiclesSerializer


@api_view(['GET', 'POST'])
def cars(request):
            if request.method == 'GET':
                vehicle_serializer = Vehicles.objects.all()
                tutorials_serializer = VehiclesSerializer(vehicle_serializer, many=True)
                return JsonResponse(tutorials_serializer.data, safe=False)
                # 'safe=False' for objects serialization

            elif request.method == 'POST':
                Controle = None
                cars_post = JSONParser().parse(request)
                vehicle_serializer = POSTCarsSerializer(data=cars_post)
                print(vehicle_serializer)
                if vehicle_serializer.is_valid():

                    make = vehicle_serializer.validated_data.get('make')
                    model = vehicle_serializer.validated_data.get('model')
                    m = str(model).lower()
                    check_models = get_models(make)
                    for i in check_models:

                        lists = str(i).lower()
                        if m == lists:
                            print('SAVED')
                            vehicle_serializer.save()
                            return JsonResponse(vehicle_serializer.data, status=status.HTTP_201_CREATED)
                        else:
                            Control = False

                    if Control == False:
                        return JsonResponse(vehicle_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                return JsonResponse(vehicle_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def carsRemove(request,pk):

           if request.method == 'DELETE':
                count = Vehicles.objects.get(car_id=pk).delete()
                return JsonResponse({'message': 'Car with id= {} was deleted successfully!'.format(pk)},
                                    status=status.HTTP_204_NO_CONTENT)
@api_view(['PUT','GET','POST'])
def carsRate(request):

    json_response = JSONParser().parse(request)
    vehicle_serializer = POSTCarsRateSerializer(data=json_response)
    if vehicle_serializer.is_valid():
        if "car_id" in json_response:
            doctor_requested_id = json_response['car_id']
            verified_object = Vehicles.objects.filter(
                car_id=doctor_requested_id)

            verified_object.update(**json_response)
            return JsonResponse({'message': "product has been updated succesfully"},status=status.HTTP_200_OK)
        else:
            return JsonResponse({'message': "product's is dosen't exist"})

@api_view(['GET'])
def carsPopular(request):
            if request.method == 'GET':
                vehicle_serializer = Vehicles.objects.all()
                tutorials_serializer = GETCarsPopularSerializer(vehicle_serializer, many=True)
                return JsonResponse(tutorials_serializer.data, safe=False)