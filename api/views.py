from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from items.models import Item
from .serializers import ItemListSerializer, DetailSerializer, UserSerializer, FavoriteSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import IsCreator
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser



# Create your views here.

class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'description', 'id']
    permission_classes = [AllowAny]

class DetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = DetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
    permission_classes = [IsCreator]