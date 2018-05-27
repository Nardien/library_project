from django.shortcuts import render
from main.forms import *
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from home.models import *
from django.db.models import Q
# Create your views here.

def main(request):
	if 'user_cid' not in request.session:
		return render(request,'main/backpage.html')
	form=Form()
	return render(request, 'main/main.html', {'form':form})

def back(request):
	if 'user_cid' in request.session:
		del request.session['user_cid']
	return render(request, 'main/backpage.html')

def search(request):
	if 'user_cid' not in request.session:
		return render(request,'main/backpage.html')
	form=request.POST['search']#please put 404 not found later one.
	ref=request.POST['ref']
	form=form.strip()
	if form=='':
		return main(request)
	
	new_form=''
	for i in form:
		if i !=' ':
			new_form+='['+i.lower()+i.upper()+']'
		else:
			new_form+=' '
	form=new_form.split()
	string='('
	string+= form[0]
	for i in form[1:]:
		string+='|' +i
	string+=')'
	if ref=="all":
		context=Book.objects.filter(Q(name__regex=string)| Q(author__regex=string) )
	elif ref=="name":
		context=Book.objects.filter(Q(name__regex=string))
	elif ref=="author" :
		context=Book.objects.filter(Q(author__regex=string))
	return render(request, 'main/search.html', {'context':context.order_by('name')})