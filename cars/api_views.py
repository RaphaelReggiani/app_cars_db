from rest_framework import viewsets
from .models import Cars, Cardata, NewUser
from .serializers import CarsSerializer, CardataSerializer, NewUserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all().order_by('-id')
    serializer_class = CarsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CardataViewSet(viewsets.ModelViewSet):
    queryset = Cardata.objects.all().order_by('-data')
    serializer_class = CardataSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class NewUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NewUser.objects.all().order_by('user_name')
    serializer_class = NewUserSerializer
    permission_classes = [AllowAny]
