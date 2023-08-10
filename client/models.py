from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
import uuid
from django.dispatch import receiver
import os
from PIL import Image
# from django.utils.text import format_lazy
# from django.utils.translation import gettext_lazy as _

# Create your models here.
IMAGE_SIZE = 800

class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField( unique=True, max_length= 50)
    email = models.EmailField( unique=True, max_length= 50)
    name = models.CharField( max_length=50, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ['email', 'name']

    objects = CustomUserManager()

    def __str__(self):
        return self.name
    

class Template(models.Model):
    themes = (('light', 'light'),
              ('dark','dark')
              )
    name = models.CharField( max_length=50)
    theme = models.CharField( max_length=6, choices= themes)
    template_file_name = models.CharField( max_length=50)

    def __str__(self):
        return f'{self.name} - {self.theme}'

class Menu(models.Model):
    id = models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False,)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=100)
    menu_link = models.CharField(max_length=100, blank=True, default= uuid.uuid4 )
    logo = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    address = models.TextField( max_length=50, blank=True)
    instagram_link = models.CharField( max_length=50, blank=True)
    facebook_link = models.CharField( max_length=50, blank=True)
    youtube_link = models.CharField( max_length=50, blank=True)
    google_link = models.CharField( max_length=50, blank=True)
    business_contact_number = models.CharField( max_length=50, blank=True)
    is_subscribed = models.BooleanField( default= False)
    qrcode = models.ImageField(upload_to='qrcodes/', null= True, blank= True)
    
    # To delete the old image when changed to new one
    def save(self, *args, **kwargs):
        if self.logo:
            try:
                this = Menu.objects.get(id=self.id)
                if this.logo != self.logo:
                    this.logo.delete(save=False)
            except: pass
            super(Menu, self).save(*args, **kwargs)
            print(self.menu_link)
            # Compressing the size of image(logo) inside save function
            img = Image.open(self.logo.path)
            output_size = (IMAGE_SIZE, IMAGE_SIZE)
            img.thumbnail(output_size)
            img.save(self.logo.path)
        else:
            super(Menu, self).save(*args, **kwargs)


    @property
    def get_image_url(self):
        if self.logo and hasattr(self.logo, 'url'):
            return self.logo.url
        else:
            return "/static/images/sadfrog.jpg"

    def __str__(self):
        return f'{self.business_name}'
    
class Header(models.Model):
    header_text = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='headers')
    description = models.CharField(max_length=50, blank= True, default="")

    # To delete the old image when changed to new one
    def save(self, *args, **kwargs):
        if self.image:
            try:
                this = Header.objects.get(id=self.id)
                if this.image != self.image:
                    this.image.delete(save=False)
            except: pass
            super(Header, self).save(*args, **kwargs)

            # Compressing the size of image(logo) inside save function
            img = Image.open(self.image.path)
            output_size = (IMAGE_SIZE, IMAGE_SIZE)
            img.thumbnail(output_size)
            img.save(self.image.path)
            print(f'none {self.image}')

           
        else:
            super(Header, self).save(*args, **kwargs)


    
    @property
    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/images/sadfrog.jpg"

    def __str__(self):
        return f'{self.menu} - {self.header_text}'
    
    
class Item(models.Model):
    # VEGNONVEG = (
    #     ('vegetarian', 'Vegetarian'),
    #     ('nonvegetarian', 'Non-Vegetarian'),
    # )
    header = models.ForeignKey(Header, on_delete=models.CASCADE)
    item_name = models.CharField( max_length=50)
    price = models.IntegerField()
    vegnonveg = models.CharField(max_length=15,)
    tags = models.CharField( max_length=50)

    def __str__(self):
        return f'{self.item_name}  {self.price}'



# To delete the image of Header Model when object is deleted
@receiver(models.signals.post_delete, sender=Header)
def auto_delete_file_on_delete_header(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

# To delete the image of Menu Model when object is deleted
@receiver(models.signals.post_delete, sender=Menu)
def auto_delete_file_on_delete_menu(sender, instance, **kwargs):
    if instance.logo:
        if os.path.isfile(instance.logo.path):
            os.remove(instance.logo.path)
