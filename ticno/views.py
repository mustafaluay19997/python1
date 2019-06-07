from django.shortcuts import render

# from .models import Books, BooksTest, Book


from django.http import HttpResponse,HttpResponseRedirect
from . import models
# from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

from ticno.models import Bookticno

# Create your views here.
def viewbookT(request,boookid):
    u = Bookticno.objects.filter(id=boookid)
    return render(request,'viewbookT.html',{'u':u})
    # return HttpResponse("hi"+boookid)

def homeT(request):
    Boo = Bookticno.objects.all()
    return render(request, 'homeT.html', {'bookst1': Boo})
    # return render(request, 'homeM.html')
# def IndexM(request):
#     return render(request, 'indexM.html')

def bookssT(request):
    Boo = Bookticno.objects.all()
    query = request.GET.get("q")
    if query:
        Boo = Boo.filter(Auther_Name__icontains=query)
    return render(request, 'indexT.html', {'bookst': Boo})

