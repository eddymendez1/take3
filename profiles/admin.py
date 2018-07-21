from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile, Credit_Cards, Shipping_Addresses


# Define an inline admin descriptor for profile model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

class Credit_CardsInline(admin.StackedInline):
    model = Credit_Cards
    can_delete = False
    verbose_name_plural = 'credit cards'

class Shipping_AddressesInline(admin.StackedInline):
    model = Shipping_Addresses
    can_delete = False
    verbose_name_plural = 'shipping addresses'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline, Credit_CardsInline,Shipping_AddressesInline,]

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)