from django.shortcuts import render
from Tapp import models
from django.http import HttpResponse
# Create your views here.
def create(request):
    s=''
    x=models.Book1(name='C++',publication_date='2019-04-21')
    x.save()
    y=models.Book1.objects.all()
    for i in y:
        s=s+i.name+" "+str(i.publication_date)+'</br>'
    # for i in y:
    #     i.delete();
    #     s = s + i.name + " " + str(i.publication_date) + '</br>'
    return HttpResponse(s)



