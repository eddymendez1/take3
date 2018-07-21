import os
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist

def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext

def upload_image_path(instance, filename):
	new_filename = instance.slug
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
	return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)

#create your model here
class ProfileManager(models.Manager):

    def new_or_get(self, request):
        profile_id = request.session.get("profile_id", None)
        qs = self.get_queryset().filter(slug=profile_id)
        if qs.count() == 1:
            new_obj = False
            profile_obj = qs.first()
            print('Profile ID Exists: ', profile_id )
            if request.user.is_authenticated and profile_obj.user is None:
                profile_obj.user = request.user
                profile_obj.save()
        else:
            profile_obj = Profile.profile_obj.newProfile(user=request.user)
            new_obj = True
            request.session['profile_id'] = profile_obj.slug
        return profile_obj, new_obj


    def newProfile(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.profile_obj.create(user = user_obj)

    # def create_profile(self, **kwargs):
    #     user = kwargs["instance"]
    #     if kwargs["created"]:
    #         user_profile = Profile(user=user)
    #         user_profile.save()
    #
    # post_save.connect(create_profile, sender=User)

# class CreditCardField(forms.IntegerField):
#     def get_cc_type(self, number):

class Profile(models.Model):
    #Column(s) = models.type (options)

    # user contains ID and password
    user        = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    # user profile img
    image       = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    #slug for id-ing whose profile
    slug        = models.SlugField(blank=True, primary_key=True)
    #Personal Information
    name        = models.CharField(max_length=120)

    #email       = models.CharField(max_length=120)

    home_addr   = models.CharField(blank=True, max_length=120)
    nick_name   = models.CharField(max_length=20)

    profile_obj = ProfileManager()

    def get_absolute_url(self):
        return "/profiles/{slug}/".format(slug=self.slug)

    # def __unicode__(self):
    #     return self.user.username

class Credit_Cards(models.Model):
    # #Credit Card Info
    user      = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    card_Holder_Name = models.CharField(max_length=120, default="John Smith")
    number = models.CharField(max_length=16, default="1234123412341234")
    expiration = models.CharField(max_length = 5, default="MM/YY")
    cvc = models.CharField(max_length= 3, default="123")

    def __str__(self):
        return self.user.username

class Shipping_Addresses(models.Model):
    #Shipping Address
    user      = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, blank=True)

    city = models.CharField(max_length=64, default="Miami")
    state = models.CharField(max_length=2, default="FL")
    zip_code = models.CharField( max_length=5, default="33199")

    def __str__(self):
        return self.user.username

def profile_pre_save_receiver(sender, instance, *args, **request):
    # profile = Profile.profile_obj.get(user=request.user)
    # instance = profile
    try:
        if not instance.profile.slug:
            instance.profile.slug = instance.username
    except ObjectDoesNotExist:
        return

pre_save.connect(profile_pre_save_receiver, sender=User)

# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()
#
# post_save.connect(save_profile, sender=User)
