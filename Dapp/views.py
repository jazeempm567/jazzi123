from django.shortcuts import render
from django.views.generic import *
# Create your views here.
from Tapp.models import *
from django.http import HttpResponse

class About(TemplateView):
    template_name="abc.html"

class BookList(ListView):
    model = Book1
    template_name = "Bookview.html"
    def Head(self,*args,**kwargs):

        lastbook=self.get_queryset().latest('publication_date')
        response=HttpResponse('')
        response['Last-Modified'] = lastbook.publication_date.strftime('%a, %d %b %Y %H:%M:%S GMT')
        return response