from django.shortcuts import render

from .models import BookBaghdad

from django.http import HttpResponse,HttpResponseRedirect
from . import models



# Create your views here.
def viewbookB(request,boookid):
    u = BookBaghdad.objects.filter(id=boookid)
    return render(request,'viewbookB.html',{'u':u})

def bookssB(request):
    Boo = BookBaghdad.objects.all()
    query = request.GET.get("q")
    if query:
        Boo = Boo.filter(Auther_Name__icontains=query)
    return render(request, 'indexB.html', {'booksb': Boo})
 

# def indexB(request):
#     return render(request, 'indexB.html')


def HomeB(request):
    Boo = BookBaghdad.objects.all()
    return render(request, 'homeB.html', {'booksb1': Boo})
