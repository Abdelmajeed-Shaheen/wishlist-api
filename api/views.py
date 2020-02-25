from django.shortcuts import render
from items.models import Item
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from .serializers import ItemListSerializer, ItemDetailSerializer, UserCreateSerializer
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from .permissions import IsAddedBy
from rest_framework.filters import OrderingFilter, SearchFilter


class UserCreateView(CreateAPIView):
    serializer_class = UserCreateSerializer


class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    permission_classes = [AllowAny,]
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['name',]


class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
    permission_classes = [IsAddedBy]
