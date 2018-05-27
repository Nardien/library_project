from django.shortcuts import render
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from home.models import *
# Create your views here.

def borrow(request, borrow):
	name=Book.objects.get(code=borrow)
	return render(request, 'book/borrow.html', {'namev':name})