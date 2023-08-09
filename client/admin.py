from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "is_staff", "is_active","phone", "name")
    list_filter = ("email", "is_staff", "is_active","phone", "name")
    fieldsets = (
        (None, {"fields": ("email", "password", "phone", "name")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "phone",
                "email","name", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)


class AdminMenu(admin.ModelAdmin):
    Menu_display = ('template', 'user', 'business_name', 'menu_link', 'logo', 'address', 'instagram_link', 'facebook_link', 'youtube_link', 'google_link', 'business_contact_number', 'is_subscribed', 'qrcode')
admin.site.register(Menu, AdminMenu)

class AdminHeader(admin.ModelAdmin):
    Header_display = ('header_text', 'image', 'menu','discription')
admin.site.register(Header, AdminHeader)

class AdminItem(admin.ModelAdmin):
    Item_display = ('item_name', 'max_length', 'vegnonveg', 'tags', 'header')
admin.site.register(Item, AdminItem)

class AdminTemplate(admin.ModelAdmin):
    Template_display = ('Template_text', 'image', 'menu', )
admin.site.register(Template, AdminTemplate)
