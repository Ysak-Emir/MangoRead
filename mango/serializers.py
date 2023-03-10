from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from mango.models import Card, Review
from users.models import User


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = "id profile_picture title year description".split()



class CardDetailSerializer(serializers.ModelSerializer):
    genre = serializers.SerializerMethodField()
    genres_type = serializers.SerializerMethodField()

    class Meta:
        model = Card
        fields = "id profile_picture title year description time_create genre genres_type".split()

    def get_genre(self, instance):
        return instance.genre.genres_title

    def get_genres_type(self, instance):
        return instance.genres_type.type_title


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "username nickname".split()


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Review
        fields = ['id', 'user', 'text', 'time_create']
        read_only_fields = ['time_create']



class ReviewCreateSerializer(serializers.Serializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_id = serializers.IntegerField()
    text = serializers.CharField(max_length=200, required=True)
    mango_id = serializers.IntegerField()

    def create(self, validated_data):
        return Review.objects.create(
            user_id=validated_data["user_id"],
            text=validated_data["text"],
            mango_id=validated_data["mango_id"]
        )
    # class Meta:
    #     model = Review
    #     fields = '__all__'

