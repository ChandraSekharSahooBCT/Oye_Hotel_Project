from django.shortcuts import render
from testapp.models import Prod
# Create your views here.
def index(request):
	p=Prod.objects.all()
	return render(request,'index.html',{'p':p})
def show(request,id):
	prod=Prod.objects.get(id=id)
	return render(request,'show.html',{'prod':prod})
def search_view(request):
    queryString=request.GET['q']
    p=Prod.objects.filter(prodname__contains=queryString)
    return render(request,'index.html',{'p':p})
