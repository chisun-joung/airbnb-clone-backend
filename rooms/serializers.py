from django.utils import timezone
from rest_framework import serializers
from .models import Amenity, Room
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
from reviews.serializers import ReviewSerializer
from medias.serializers import PhotoSerializer
from wishlists.models import Wishlist
from bookings.models import Booking


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "pk",
            "name",
            "description",
        )


class RoomDetailSerializer(serializers.ModelSerializer):
    owner = TinyUserSerializer(read_only=True)
    category = CategorySerializer(
        read_only=True,
    )
    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    photos = PhotoSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Room
        fields = "__all__"

    def get_rating(self, room):
        return room.rating()

    def get_is_owner(self, room):
        if self.context.get("request"):
            return room.owner == self.context["request"].user
        return False

    def get_is_liked(self, room):
        request = self.context.get("request")
        if request:
            if request.user.is_authenticated:
                return Wishlist.objects.filter(
                    rooms__pk=room.pk,
                    user=request.user,
                ).exists()
        return False


class RoomListSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    photos = PhotoSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
            "rating",
            "is_owner",
            "photos",
        )

    def get_rating(self, room):
        return room.rating()

    def get_is_owner(self, room):
        if self.context.get("request"):
            return room.owner == self.context["request"].user
        return False


class CreateRoomBookingSerializer(serializers.ModelSerializer):
    check_in = serializers.DateField()
    check_out = serializers.DateField()

    class Meta:
        model = Room
        fields = (
            "check_in",
            "check_out",
            "guests",
        )

    def validate_check_in(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Check in date is in the past")
        return value

    def validate_check_out(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Check out date is in the past")
        return value

    def validate(self, data):
        if data["check_out"] <= data["check_in"]:
            raise serializers.ValidationError(
                "Check out date must be after check in date"
            )
        if Booking.objects.filter(
            check_in__lte=data["check_out"],
            check_out__gte=data["check_in"],
        ).exists():
            raise serializers.ValidationError("Room is not available")
        return data
