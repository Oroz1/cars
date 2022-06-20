from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Программный менеджер для регистрации пользователя через shell 
class CustomAccountManager(BaseUserManager):
    
    def create_superuser(self, username, name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(username, name, password, **other_fields)

    def create_user(self, username, name, password, **other_fields):

        user = self.model(username=username,
                          name=name, **other_fields)
        user.set_password(password)
        user.save()
        return user


# Таблица пользователя 
class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = 'Пользователи'

    avatar = models.ImageField(upload_to='avatars/', verbose_name='аватарка', null=True, blank=True)
    username = models.CharField(max_length=150, unique=True, verbose_name='Имя пользователя')
    name = models.CharField(max_length=150, blank=True, verbose_name='Полная имя')
    email = models.EmailField(verbose_name='Элетронная почта', null=True, blank=True)
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона', null=True)
    information = models.TextField(verbose_name='Информация о пользователе', null=True, blank=True)
    is_staff = models.BooleanField(default=False, verbose_name='Статус персонала')
    is_active = models.BooleanField(default=False, verbose_name='Подтверждение по почте')
    is_superuser = models.BooleanField(default=False, verbose_name='Статус администратора')
    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name',]

    def __str__(self):
        return f'{self.username}'


class TimeStampMixin(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата добавление')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата изменения')

    class Meta:
        abstract = True


class Currencies(TimeStampMixin):

    class Meta:
        verbose_name = 'валюта'
        verbose_name_plural = 'валюты'
        ordering = ['-created_at']

    title = models.CharField(max_length=100, verbose_name='название валюты')

    def __str__(self):
        return f'{self.title}'


class Images(TimeStampMixin):
    
    class Meta:
        verbose_name = 'фотография'
        verbose_name_plural = 'фотографий'
        ordering = ['-created_at']

    title = models.CharField(max_length=100, verbose_name='название фотографий', null=True)
    image = models.ImageField(upload_to='cars_images/%Y/%m/%d/', verbose_name='изображение')

    def __str__(self):
        return f'{self.title}'


class Brands(TimeStampMixin):
    
    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'
        ordering = ['-created_at']

    title = models.CharField(max_length=100, verbose_name='название марки')

    def __str__(self):
        return f'{self.title}'


class Models(TimeStampMixin):
    
    class Meta:
        verbose_name = 'модель машины'
        verbose_name_plural = 'модели машины'
        ordering = ['-created_at']

    title = models.CharField(max_length=100, verbose_name='название модели')

    def __str__(self):
        return f'{self.title}'


class TypeOfCars(TimeStampMixin):
    
    class Meta:
        verbose_name = 'вид машины'
        verbose_name_plural = 'виды машин'
        ordering = ['-created_at']

    title = models.CharField(max_length=100, verbose_name='название типа машины')

    def __str__(self):
        return f'{self.title}'


class Gearboxes(TimeStampMixin):
    
    class Meta:
        verbose_name = 'тип КПП'
        verbose_name_plural = 'типы КПП'
        ordering = ['-created_at']

    title = models.CharField(max_length=100, verbose_name='название типа КПП')

    def __str__(self):
        return f'{self.title}'


class TypeOfDrives(TimeStampMixin):
    
    class Meta:
        verbose_name = 'тип привода'
        verbose_name_plural = 'типы приводов'
        ordering = ['-created_at']

    title = models.CharField(max_length=100, verbose_name='название типа привода')

    def __str__(self):
        return f'{self.title}'


class FuelTypes(TimeStampMixin):
    
    class Meta:
        verbose_name = 'вид топлива'
        verbose_name_plural = 'виды топлива'
        ordering = ['-created_at']

    title = models.CharField(max_length=100, verbose_name='название вида топлива')

    def __str__(self):
        return f'{self.title}'


class Cars(TimeStampMixin):

    class Meta:
        verbose_name = 'машина'
        verbose_name_plural = 'машины'
        ordering = ['-created_at']

    
    title = models.CharField(max_length=255, verbose_name='название')
    price = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='стоисомть')
    currency = models.ForeignKey('Currencies', null=True, on_delete=models.SET_NULL, verbose_name='валюта')
    images = models.ManyToManyField('Images', verbose_name='фотографий', related_name='cars')
    description = models.CharField(max_length=1200, verbose_name='описание', help_text='Максимальная количество символов 255')
    brand = models.ForeignKey('Brands', null=True, on_delete=models.SET_NULL, verbose_name='марка')
    model = models.ForeignKey('Models', null=True, on_delete=models.SET_NULL, verbose_name='модель')
    type_of_car = models.ForeignKey('TypeOfCars', null=True, on_delete=models.SET_NULL, verbose_name='вид машины')
    year_of_issue = models.PositiveIntegerField(verbose_name='год выпуска')
    volume = models.DecimalField(verbose_name='объем', decimal_places=1, max_digits=2)
    gearbox = models.ForeignKey('Gearboxes', null=True, on_delete=models.SET_NULL, verbose_name='КПП')
    type_of_drive = models.ForeignKey('TypeOfDrives', null=True, on_delete=models.SET_NULL, verbose_name='привод')
    fuel_type = models.ForeignKey('FuelTypes', null=True, on_delete=models.SET_NULL, verbose_name='тип топлива')
    views = models.PositiveIntegerField(verbose_name='Просмотры', default=0)
    owner = models.ForeignKey('User', null=True, on_delete=models.CASCADE, verbose_name='владелец')

    def __str__(self):
        return f'{self.title}'
    
# Create your models here.
