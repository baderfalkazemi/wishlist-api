from rest_framework import serializers
from items.models import Item, FavoriteItem
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class ItemListSerializer(serializers.ModelSerializer):
    added_by = UserSerializer()
    detail = serializers.HyperlinkedIdentityField(
        view_name = "api-detail",
        lookup_field = "id",
        lookup_url_kwarg = "item_id"
        )
    class Meta:
        model = Item
        fields = ['image', 'name', 'detail', 'added_by']

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        field = ['user']

class DetailSerializer(serializers.ModelSerializer):
    favorited_by = serializers.SerializerMethodField()
    count = serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields = ['image', 'name', 'description', 'id', 'favorited_by', 'count']

    def get_favorited_by(self, obj):
        favs = obj.favoriteitem_set.all()
        return FavoriteSerializer(favs, many=True).data

    def get_count(self, obj):
        favs = obj.favoriteitem_set.all()
        return favs.count()
