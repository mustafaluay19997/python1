"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainn.views import bookss,Register,registr_backend,Log,Log_Backend,home,viewbook,viewbook1,viewbook2,anmar,ali #import views main
from lib.views import viewbookM,homeM,bookssM  #import views mustanseraiy
from bagdad.views import viewbookB,bookssB,HomeB  #import views baghdad
from ticno.views import viewbookT,homeT,bookssT #import views ticno


urlpatterns = [
    path('admin/', admin.site.urls),
    
# main
    path('', home, name='home'),
# register main
    path('register/', Register, name='Register'),
    path('registr_backend/', registr_backend, name='registr_backend'),
# logIn main
    path('login/', Log, name='Log'),
    path('logBackend/', Log_Backend, name='Log_Backend'),
#book main
    path('viewbook/<str:boookid>',viewbook,name='viewbook'),# book main
    path('viewbook1/<str:boookid1>',viewbook1,name='viewbook1'),# book main
    path('viewbook2/<str:boookid1>',viewbook2,name='viewbook2'),# book main
    path('books/', bookss, name='books'),
# cv programer
    path('anmar/', anmar, name='anmar'),
    path('ali/', ali, name='ali'),

########################################################


# mustanseraiy lib
    path('homeM/', homeM, name='homeM'),
    # path('indexM/', IndexM, name='indexM'),
    path('bookssM/', bookssM, name='booksM'),
    path('viewbookM/<str:boookid>',viewbookM,name='viewbookM'),

########################################################

    # bagdad
    path('viewbookB/<str:boookid>',viewbookB,name='viewbookB'),
    path('bookssB/', bookssB, name='booksB'),
    # path('indexB/', indexB, name='indexB'),
    path('homeB/', HomeB, name='homeB'),

########################################################

    # ticno
    path('viewbookT/<str:boookid>',viewbookT,name='viewbookT'),
    path('bookssT/', bookssT, name='bookssT'),
    path('homeT/', homeT, name='homeT'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
