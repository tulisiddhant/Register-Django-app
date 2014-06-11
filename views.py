from django.shortcuts import render
from django.http import HttpResponse
from register.models import Person

def index(request):
	return render(request, 'register/index.html', {})

def register(request):
	return render(request, 'register/register.html', {})

def thanks(request):
	Person(f_name=request.POST['fname'], l_name=request.POST['lname'], age=request.POST['age']).save()
	return HttpResponse("thanks")

def see_list(request):
	list_all = Person.objects.all()
	context = {'list_all': list_all }
	return render(request, 'register/list.html', context)

def individual(request, per_id):
	return HttpResponse("You're looking at person %s." %per_id)
	
