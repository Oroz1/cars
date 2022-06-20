from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
from PIL import Image
from .models import Cars, User


@receiver(pre_delete, sender=Cars)
def pre_delete_cars(instance, **kwargs):
    instance.images.all().delete()


@receiver(post_save, sender=User)
def post_save_user(instance, created, **kwargs):
    if created:
        if instance.avatar:
            image = Image.open(instance.avatar)

            if image.height < image.width:
                x = (int(image.width) - int(image.height)) / 2
                y = 0
                h = image.height
                w = image.height
               
            elif image.height > image.width:
                y = (int(image.height) - int(image.width)) / 2
                x = 0
                h = image.width
                w = image.width
            
            cropped_image = image.crop((x, y, w, h))
            resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
            resized_image.save(instance.avatar.path)
        else:
            instance.avatar = '/img/user.png'
            instance.save()
        return instance