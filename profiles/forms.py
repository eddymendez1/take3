from .models import Profile as ProfileModel

from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def validateEmail(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

class ProfileForm(forms.Form):

	# class Meta:
	# 	model = ProfileModel
	# 	fields = ['name', 'nick_name', 'home_addr']
		name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Full name"}))
		nick_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Nick name"}))
		#email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Email"}))
		home_addr = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Home Address"}))

		#address
		# address_1 = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Address 1"}))
		# address_2 = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Address 2"}))
        #
		# city = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "City"}))
		# state = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "State"}))
		# zip_code = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Zip Code"}))

		#image = forms.ImageField()

		def clean(self):
			cleaned_data = super(ProfileForm, self).clean()
			name = cleaned_data.get('name')
			nick_name = cleaned_data.get('nick_name')
			home_addr = cleaned_data.get('home_addr')
			#image = cleaned_data.get('image')
			# if not name and not nick_name:
			# 	raise forms.ValidationError('Missing Required Fields')
			return cleaned_data
