from django.forms import ModelForm
from .models import *

class SubmitForm(ModelForm):
	class Meta:
		model = submit
		fields = '__all__'

class PostsForm(ModelForm):
	class Meta:
		model = posts
		fields = '__all__'