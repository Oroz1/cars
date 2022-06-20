from dataclasses import fields
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from .models import *




class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('id', 'username', 'name', 'phone_number', 'email')
    list_display = ('id', 'username', 'get_avatar', 'name', 'phone_number', 'email', 'last_login')
    list_display_links = ('id', 'name', 'username',)
    fieldsets = (
        (None, {'fields': ('avatar', 'get_avatar', 'username', 'name', 'email', 'information', 'phone_number', 'is_active', 'is_superuser', 'password',)},
         ),
    )
    add_fieldsets = (
        (None, {
            'fields': ('avatar', 'username', 'name', 'email', 'phone_number', 'information', 'password1', 'password2', 'is_superuser', 'is_active')}
         ),
    )
    readonly_fields = ('last_login', 'get_avatar',)


    def get_avatar(self, obj):
        try:
            return mark_safe(f'<img src="{obj.avatar.url}" width="50rem">')
        except Exception:
            return None

    get_avatar.short_description = 'Аватарка'


admin.site.register(User, UserAdminConfig)


@admin.register(Currencies)
class CurrenciesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',) 
    list_display_links = ('id', 'title',)
    search_fields = ('title', )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_image') 
    list_display_links = ('id', 'title',)
    search_fields = ('title', )
    readonly_fields = ('created_at', 'updated_at', 'get_image',)
    fields = ('title', 'image', 'get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="30%">') 

    get_image.short_description = 'Изображение'


@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',) 
    list_display_links = ('id', 'title',)
    search_fields = ('title', )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Models)
class ModelsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',) 
    list_display_links = ('id', 'title',)
    search_fields = ('title', )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(TypeOfCars)
class TypeOfCarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',) 
    list_display_links = ('id', 'title',)
    search_fields = ('title', )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Gearboxes)
class GearboxesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',) 
    list_display_links = ('id', 'title',)
    search_fields = ('title', )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(TypeOfDrives)
class TypeOfDrivesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',) 
    list_display_links = ('id', 'title',)
    search_fields = ('title', )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(FuelTypes)
class FuelTypesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',) 
    list_display_links = ('id', 'title',)
    search_fields = ('title', )
    readonly_fields = ('created_at', 'updated_at')


class CarsAdminForm(forms.ModelForm):

    class Meta:
        model = Cars 
        fields = '__all__'

        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'vIntegerField', 'step': '0.001'}),
            'volume': forms.NumberInput(attrs={'class': 'vIntegerField', 'step': '0.1'}),
        }


@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'model', 'year_of_issue', 'price', 'owner') 
    list_display_links = ('id', 'title',)
    form = CarsAdminForm
    list_filter = (
        'currency',
        'brand',
        'model',
        'type_of_car',
        'type_of_drive',
        'fuel_type',
        'owner',
    )

    search_fields = ('title', )
    readonly_fields = ('created_at', 'updated_at', 'get_images', 'views',)
    fields = (
        'title',
        'price',
        'currency',
        'images',
        'description',
        'brand',
        'model',
        'type_of_car',
        'year_of_issue',
        'volume',
        'gearbox',
        'type_of_drive',
        'fuel_type',
        'owner',
        'views',
        'get_images',
    )

    def get_images(self, obj):
        temp = ''
       
        for image in obj.images.all().values():
            url = '/media/' + image["image"]
            temp += f'<div class="mb-2"><img src="{url}" class="w-50" /></div>'
        return mark_safe(temp)
    
    get_images.short_description = 'Фотографий'
# Register your models here.
