from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from core.models import *
from .serializers import *
from .permissions import IsOwnerPermission, IsOwnerImagePermission


class PaginationApi(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 20


class CurrenciesApiView(ListAPIView):
    queryset = Currencies.objects.all()
    serializer_class = CurrenciesSerializer
    permission_classes = (AllowAny,)


class CurrenciesDetailApiView(RetrieveAPIView):
    queryset = Currencies.objects.all()
    serializer_class = CurrenciesSerializer
    permission_classes = (AllowAny,)


class ImagesApiView(ListAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    permission_classes = (AllowAny,)
    pagination_class  = PaginationApi


class ImagesDetailApiView(RetrieveAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    permission_classes = (AllowAny,)


class ImagesCreateApiView(CreateAPIView):
    serializer_class = ImagesSerializer
    permission_classes = (IsAuthenticated,)


class ImagesDeleteApiView(RetrieveDestroyAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    permission_classes = (IsAuthenticated, IsOwnerImagePermission)


class UserApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class UserDetailApiView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class BrandsApiView(ListAPIView):
    queryset = Brands.objects.all()
    serializer_class = BrandsSerializer
    permission_classes = (AllowAny,)


class BrandsDetailApiView(RetrieveAPIView):
    queryset = Brands.objects.all()
    serializer_class = BrandsSerializer
    permission_classes = (AllowAny,)


class ModelsApiView(ListAPIView):
    queryset = Models.objects.all()
    serializer_class = ModelsSerializer
    permission_classes = (AllowAny,)


class ModelsDetailApiView(RetrieveAPIView):
    queryset = Models.objects.all()
    serializer_class = ModelsSerializer
    permission_classes = (AllowAny,)


class TypeOfCarsApiView(ListAPIView):
    queryset = TypeOfCars.objects.all()
    serializer_class = TypeOfCarsSerializer
    permission_classes = (AllowAny,)


class TypeOfCarsDetailApiView(RetrieveAPIView):
    queryset = TypeOfCars.objects.all()
    serializer_class = TypeOfCarsSerializer
    permission_classes = (AllowAny,)


class GearboxesApiView(ListAPIView):
    queryset = Gearboxes.objects.all()
    serializer_class = GearboxesSerializer
    permission_classes = (AllowAny,)


class GearboxesDetailApiView(RetrieveAPIView):
    queryset = Gearboxes.objects.all()
    serializer_class = GearboxesSerializer
    permission_classes = (AllowAny,)


class FuelTypesApiView(ListAPIView):
    queryset = FuelTypes.objects.all()
    serializer_class = FuelTypesSerializer
    permission_classes = (AllowAny,)


class FuelTypesDetailApiView(RetrieveAPIView):
    queryset = FuelTypes.objects.all()
    serializer_class = FuelTypesSerializer
    permission_classes = (AllowAny,)


class CarsApiView(ListAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    permission_classes = (AllowAny,)
    pagination_class  = PaginationApi


class CarsDetailApiView(RetrieveAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    permission_classes = (AllowAny,)


class CarsCreateApiView(CreateAPIView):
    serializer_class = CarsCreateUpdateSerializer
    permission_classes = (IsAuthenticated,)


class CarsUpdateApiView(RetrieveUpdateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsCreateUpdateSerializer
    permission_classes = (IsAuthenticated, IsOwnerPermission)


class CarsDeleteApiView(RetrieveDestroyAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsCreateUpdateSerializer
    permission_classes = (IsAuthenticated, IsOwnerPermission)


class RegistrationAPI(GenericAPIView):
    serializer_class = CreateUserProfileSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        password = make_password(self.request.data['password'])
        serializer.is_valid(raise_exception=True)
        user = serializer.save(password=password)
        token = Token.objects.get_or_create(user=user)[0].key
        data = {}
        data["message"] = "user registered successfully"
        data["username"] = user.username
        data["token"] = token
        return Response(data, status=200)