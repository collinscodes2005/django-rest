from rest_framework.response import Response
from base.models import Item
from .serializers import ItemSerializers
from rest_framework.decorators import api_view

@api_view(['GET'])

def get_data(request):

    items = Item.objects.all()
    serializer = ItemSerializers(items, many=True)


    return Response(serializer.data)


