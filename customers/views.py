from django.http import JsonResponse
from customers.models import Customer
from customers.serializers import CustomerSerializer, UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated #authentication

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated]) # authentication decorator
def customers(request):
    if request.method == 'GET':
        #invoke serializer and return to client
        data = Customer.objects.all() #get all from customer
        serializer = CustomerSerializer(data, many=True)
        return Response({'customers': serializer.data})
    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'customer': serializer.data}, status=status.HTTP_201_CREATED) # key customer
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE']) # DECORATORS
@permission_classes([IsAuthenticated])
def customer(request, id):
    try:
        data = Customer.objects.get(pk=id) #get only specified - id
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  
    if request.method == "GET":  
        serializer = CustomerSerializer(data)
        return JsonResponse({'customer': serializer.data})
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'POST':
        serializer = CustomerSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'customer': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)







"""
Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes 
that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, 
allowing parsed data to be converted back into complex types, after first validating the incoming data.
"""