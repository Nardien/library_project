from django.forms import ModelForm
from main.models import *

class Form(ModelForm):
	class Meta:
		model=Search
		fields=['name']