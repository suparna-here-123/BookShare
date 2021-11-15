"""bookshareApplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from userApp import views
from lenderBorrower import views as v
from dashboard import views as v1



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('validate/',views.validate),
    path('register/',views.register),
    path('register/user/',views.add_user),
    path('lender2/',v.lender2),
    path('lenderBorrower/lender2/',v.display,name='lender2'),
    #path('borrower/',v.borrower),
    path('dashboard/home/',v1.available),
    path('dashboard/home/',v1.lendable),
    path('lend/',v.lend),
    path('lend/user/',v.add_book),
    path('backtodash/',v.backtodash),
    path('profile2/',v.profile2),
    path('dashboard/home/',v1.profile),
    path('borrowdetails/<bookId>',v.borrowdetails),
    path('confirmborrow/<bookId>',v.confirmborrow),
    path('lenderBorrower/home/',v.borrow),
    path('delete/<bookId>',v.deletebook),
  
    
    
    
    


    
]
