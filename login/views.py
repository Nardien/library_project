from django.shortcuts import render
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from home.models import *
from main import views
from django.http import HttpResponse
# Create your views here.
def login(request):
	if request.method =='GET':
		if 'user_cid' in request.session: 
			return render(request, 'login/success.html')
		else:
			return render(request,'login/log.html')
	elif request.method=='POST':
		try:
			context=Client.objects.get(cid=request.POST["user_cid"])
			print(context.cid)
			request.session['user_cid']=context.cid
			print('pass')
			return render(request, 'login/success.html')
		except:
			return render(request, 'login/log.html',{'loginfail': 'This is not registered user'})