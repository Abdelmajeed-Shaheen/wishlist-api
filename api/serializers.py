from rest_framework import serializers
from items.models import Item, FavoriteItem
from django.contrib.auth.models import User

class UserCreateSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ['username', 'password']
	def create(self, validated_data):
		username = validated_data['username']
		password = validated_data['password']
		new_user = User(username=username)
		new_user.set_password(password)
		new_user.save()
		return validated_data


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['first_name', 'last_name',]


class ItemListSerializer(serializers.ModelSerializer):
	favourited = serializers.SerializerMethodField()
	added_by = UserSerializer()
	detail = serializers.HyperlinkedIdentityField(
    view_name = "api-detail",
    lookup_field = "id",
    lookup_url_kwarg = "item_id",
    )
	class Meta:
		model = Item
		fields = ['name','detail','favourited','added_by']
	def get_favourited(self, obj):
		return len(obj.favoriteitem_set.all())


class ItemDetailSerializer(serializers.ModelSerializer):
	favourited_by = serializers.SerializerMethodField()
	class Meta:
		model = Item
		fields = ['id','image','name','description','added_by','favourited_by',]
	def get_favourited_by(self, obj):
		 favs = obj.favoriteitem_set.all()
		 return FavoriteItemSerializer(favs, many=True).data


class FavoriteItemSerializer(serializers.ModelSerializer):
	user=UserSerializer()
	class Meta:
		model = FavoriteItem
		fields = ['user']
