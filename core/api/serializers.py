from rest_framework import serializers
from core.models import *


class UserSerializer(serializers.ModelSerializer):
     class Meta:
        model = User
        fields = (
            'avatar',
            'username',
            'name',
            'email',
            'phone_number',
            'information',
        )


class CurrenciesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Currencies
        fields = '__all__'


class ImagesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Images
        fields = '__all__'


class BrandsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Brands
        fields = '__all__'


class ModelsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Models
        fields = '__all__'


class TypeOfCarsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TypeOfCars
        fields = '__all__'


class GearboxesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Gearboxes
        fields = '__all__'


class TypeOfDrivesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TypeOfDrives
        fields = '__all__'


class FuelTypesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FuelTypes
        fields = '__all__'


class TypeOfCarsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TypeOfCars
        fields = '__all__'


class CarsSerializer(serializers.ModelSerializer):

    currency = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='title'
    )

    images = ImagesSerializer(many=True)

    brand = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='title'
    )

    model = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='title'
    )

    type_of_car = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='title'
    )

    gearbox = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='title'
    )

    type_of_drive = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='title'
    )

    fuel_type = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='title'
    )

    owner = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Cars
        fields = '__all__'


class CarsCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cars
        fields = '__all__'



class CreateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'avatar'
            'username',
            'name',
            'email',
            'phone_number',
            'information',
            'password',
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.save()
        return user