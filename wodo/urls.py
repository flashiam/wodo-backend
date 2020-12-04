from django.urls import path

from . import views, call_api, user, workerCall, hirings, createOrder

urlpatterns = [
    path('worker', views.showFilter, name='home'),
    path ('call', call_api.custCalls, name='call'),
    path('skill', views.skillList, name='skill'),
    path('test', views.testJson, name='test'),
    path('all', views.allWorkers, name='all'),
    path('cache', views.filterData, name='cache'),
    path('first', views.firstCall, name='first'),
    path('checkUser', user.checkUser, name='checkuser'),
    path('createUser', user.createUser, name='createuser'),
    path('checkBalance', views.checkBalance, name='checkBalance'),
    path('walletBalance', views.WalletBalance, name='walletBalance'),
    path('walletData', views.WalletParas, name='WalletData'),
    path('AddBalance', views.AddWodoMoney, name='AddBalance'),
    path('DedBalance', views.DedWodoMoney, name='DedBalance'),
    path('contact', workerCall.getContact, name='contact'),
    path('ratings', views.showRat, name='rating'),
    path('save', hirings.saveWorkers, name='save'), 
    path('hire', views.hireWorker, name='hire'),
    path('deny', views.dutyDenial, name='denial'),
    path('userHistory', views.historyWatch, name='userHistory'),
    path('getOrderId', createOrder.createOrder, name='getOrderId')
]


# http://api.wodoworker.com/filter/contact?CallFrom=9893292998&CallTo=7987332031&CallSid=12345&Direction=Incoming&Created=2020-11-29 21:51:10&StartTime=2020-11-29 21:51:10&CurrentTime=