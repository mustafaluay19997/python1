from django.shortcuts import render,redirect

# ######
from django.contrib import messages

######


# from .models import  Book
from lib.models import  BookMust
from bagdad.models import BookBaghdad
from ticno.models import Bookticno

from django.http import HttpResponse,HttpResponseRedirect
from . import models
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User



# Create your views here.
def viewbook(request,boookid):
    b = BookBaghdad.objects.filter(id=boookid)
    return render(request,'viewbook.html',{'b':b })
    
def viewbook1(request,boookid1):
    m = BookMust.objects.filter(id=boookid1)
    return render(request,'viewbook1.html',{'m':m })

def viewbook2(request,boookid1):
    t = Bookticno.objects.filter(id=boookid1)
    return render(request,'viewbook2.html',{'t':t })

def home(request):
    return render(request, 'home.html')

# cv programer
def anmar(request):
    return render(request, 'anmar.html')

def ali(request):
    return render(request, 'ali.html')



def bookss(request):

    # request book from baghdad
    Boo = BookBaghdad.objects.all()
    query = request.GET.get("q")
    if query:
        Boo = Boo.filter(Book_Name__icontains=query)

    # request book from mustatsery
    Boo1 = BookMust.objects.all()
    query1 = request.GET.get("q")
    if query1:
        Boo1 = Boo1.filter(Auther_Name__icontains=query)
    # request book from Bookticno   
    Boo2 = Bookticno.objects.all()
    query2 = request.GET.get("q")
    if query2:
        Boo1 = Boo1.filter(Auther_Name__icontains=query)

    return render(request, 'index.html', {'books1': Boo,'books2': Boo1,'books3':Boo2})

    #########################################################
            ############## register  ##############
    #########################################################


def Register(request):
    return render(request, 'register.html')


def registr_backend(request):
    try:
        user = User.objects.create_user(request.POST['username'], request.POST['e-mail'], request.POST['pass'])
        user.first_name = request.POST['FirstName']
        user.last_name = request.POST['LastName']
        user.save()
        return render(request, 'login.html')
    except:
        return render(request, 'register.html')

    #######################################################
             ############## log in  ##############
    #######################################################


def Log(request):
    return render(request, 'login.html', {})


def profile(request, username):
    return render(request, 'profile.html', {'u': username})


# def Log_Backend(request):
#     u = request.POST['username']
#     p = request.POST['password']
#     re = authenticate(username=u, password=p)
#     if re is None:
#         print('log in')
#         login(request, re)
#         link = '/login/'
#         messages.warning(request,'errore in user name or password')
#         return HttpResponseRedirect(link)

#     #  return render(request,'books.html')
#     else:
#         link1 = '/books/'
#         return HttpResponseRedirect(link1)



def logout_view(request):
    logout(request)
    # Redirect to a success page.


def Log_Backend(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            link1 = '/books/'
            return HttpResponseRedirect(link1)
            # Redirect to a success page.
        else:
            messages.warning(request,'errore in user name or password')
            # Return a 'disabled account' error message
    else:
        # Return an 'invalid login' error message.
        login(request, user)
        link = '/login/'
        return HttpResponseRedirect(link)


#  if request.method=='POST':
#             u = request.POST['username']
#             p = request.POST['password']
#             user = authenticate(request, username=u, password=p)
#             if user is not None:
#                 login(request,user)
#                 # link = '/login/'
#                 return HttpResponseRedirect('login')
#             else:
#                 messages.warning(request,'errore in user name or password')
#                 # link1 = '/books/'
#             return render(request,'books')

    