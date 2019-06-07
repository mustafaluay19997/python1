from django.shortcuts import render

# from .models import Books, BooksTest, Book


from django.http import HttpResponse,HttpResponseRedirect
from . import models
# from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

from lib.models import BookMust

# Create your views here.
def viewbookM(request,boookid):
    u = BookMust.objects.filter(id=boookid)
    return render(request,'viewbookM.html',{'u':u})
    # return HttpResponse("hi"+boookid)

def homeM(request):
    Boo = BookMust.objects.all()
    return render(request, 'homeM.html', {'booksm1': Boo})
    # return render(request, 'homeM.html')
# def IndexM(request):
#     return render(request, 'indexM.html')
 
def bookssM(request):
    Boo = BookMust.objects.all()
    query = request.GET.get("q")
    if query:
        Boo = Boo.filter(Auther_Name__icontains=query)
    return render(request, 'indexM.html', {'booksm': Boo})


   
   