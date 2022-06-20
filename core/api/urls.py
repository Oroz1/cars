from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view
from .views import *

urlpatterns = [
    path('swagger/', get_swagger_view(title='Cars API')),
    path('login/', obtain_auth_token),
    path('registration/', RegistrationAPI.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('currencies/', CurrenciesApiView.as_view()),
    path('currencies/<int:pk>/', CurrenciesDetailApiView.as_view()),

    path('images/', ImagesApiView.as_view()),
    path('images/<int:pk>/', ImagesDetailApiView.as_view()),
    path('images/create', ImagesCreateApiView.as_view()),
    path('images/<int:pk>/delete', ImagesDeleteApiView.as_view()),

    path('user/', UserApiView.as_view()),
    path('user/<int:pk>/', UserDetailApiView.as_view()),

    path('brands/', BrandsApiView.as_view()),
    path('brands/<int:pk>/', BrandsDetailApiView.as_view()),

    path('models/', ModelsApiView.as_view()),
    path('models/<int:pk>/', ModelsDetailApiView.as_view()),

    path('type_of_cars/', TypeOfCarsApiView.as_view()),
    path('type_of_cars/<int:pk>/', TypeOfCarsDetailApiView.as_view()),

    path('gearboxes/', GearboxesApiView.as_view()),
    path('gearboxes/<int:pk>/', GearboxesDetailApiView.as_view()),

    path('fuel_types/', FuelTypesApiView.as_view()),
    path('fuel_types/<int:pk>/', FuelTypesDetailApiView.as_view()),

    path('currencies/', CurrenciesApiView.as_view()),
    path('currencies/<int:pk>/', CurrenciesApiView.as_view()),

    path('cars/', CarsApiView.as_view()),
    path('cars/<int:pk>/', CarsDetailApiView.as_view()),
    path('cars/create/', CarsCreateApiView.as_view()),
    path('cars/<int:pk>/update/', CarsUpdateApiView.as_view()),
    path('cars/<int:pk>/delete/', CarsDeleteApiView.as_view()),
]
