from django.http import JsonResponse
from customers.models import Customer
from customers.serializers import CustomerSerializer


def customers(request):
    #invoke serializer and return to client
    data = Customer.objects.all() #get all from customer
    serializer = CustomerSerializer(data, many=True)
    return JsonResponse({'customers': serializer.data})

def customer(resquest, id):
    data = Customer.objects.get(pk=id) #get only specified - id
    serializer = CustomerSerializer(data)
    return JsonResponse({'customer': serializer.data})



"""
Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes 
that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, 
allowing parsed data to be converted back into complex types, after first validating the incoming data.
"""