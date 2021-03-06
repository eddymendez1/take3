import random
import os
from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from django.urls import reverse
from django.utils import timezone

def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext

def upload_image_path(instance, filename):
	new_filename = random.randint(1, 395747514215)
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
	return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)

class ProductManager(models.Manager):
	def get_by_id(self, id):
		qs = self.get_queryset().filter(id=id)
		if qs.count() == 1:
			return qs.first()
		return None

class Product(models.Model):
	title		= models.CharField(max_length=120)
	author		= models.CharField(max_length=120, default='Unknown')
	slug		= models.SlugField(blank=True, unique=True)
	genre		= models.CharField(max_length=120, default='Unknown')
	description = models.TextField()
	rates		= models.IntegerField(default=1)
	price		= models.DecimalField(decimal_places=2, max_digits=10, default=100.00)
	image		= models.ImageField(upload_to=upload_image_path, null=True, blank=True)
	#image		= models.FileField(upload_to='products/', null=True, blank=True)
	quantity 	= models.IntegerField(default=1)
	featured	= models.BooleanField(default=False)  # also can be Best Seller
	amountsold	= models.IntegerField(default=0)

	objects = ProductManager()

	def get_absolute_url(self):
		return "/products/{slug}/".format(slug=self.slug)
		#return reverse("products:detail", kwargs={"slug":self.slug})

	def __str__(self):
		return self.title

def product_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)


class Comment(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text