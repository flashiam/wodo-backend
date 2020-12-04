from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from wodo.models import hired, workers, appUser, transaction, saved, dutyDenials, workRating
import json
import math
import datetime
import pytz

def checkTime(time):
    start_m = datetime.time(6, 00, 00)
    end_m = datetime.time(14, 00, 00)
    x = datetime.time(int(time))
    if start_m <= end_m:
        morning = start_m <= x <= end_m
    else:
        morning = start_m <= x or x <= end_m

    if morning is True:
        slot = "MORNING"
    else:
        slot = "EVENING"
    
    return slot

def checkDate(date):
    dat = date
    today = datetime.date.today()
    # date = datetime.date(dat)
    if today == date:
        status = "ONGOING"
    elif today > date:
        status = "COMPLETED"
    else:
        status = "UPCOMING"

    return status 

def showSchd(wid):
    worker = workers.objects.filter(workerid=wid)
    
    if len(worker)!=0:
        response = {
            "status": "Failure",
            "data": "Invalid worker details"
        }
    

    h = hired.objects.filter(workerIDH=worker[0])
    fins = []

    if len(h)!=0:

        for x in h:
            data = {
                "date": x.date,
                "slot": x.slot,
                "status": x.status,
                "transid": x.orderid,
                "timestamp": x.updated_at
                }
            fins.append(data)
        response = {
            "Status": "Success",
            "data": fins,
        }
    else:
        response = {
            "status": "Failure",
            "data": "No hiring data available for this worker."
        }
    return response
    
def hire(wid, uid, tid, slot, date):

    y = int(date[0:4])
    m = int(date[5:7])
    d = int(date[8:10])

    
    worker = workers.objects.filter(workerid=wid)
    if len(worker)==0:
        response ={
            "status":"Failed",
            "data": "Invalid worker token value."
            }
    
    user = appUser.objects.filter(username=uid)
    if len(user)==0:
        response={
            "status":"Failed",
            "date": "Invalid User token value."
            }
   
    trans = transaction.objects.filter(transID=tid)

    if len(trans)==0 or trans[0].purpose!="HIRING":
        response={
            "status":"Failure",
            "data": "Invalid Transaction ID"
        }
        return response
    
    hires = hired.objects.filter(orderid=trans[0])

    now = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%H")
    if len(hires)==0: 
        if checkDate(datetime.date(y, m, d))=="ONGOING":
            if checkTime(now)==slot:
                hire = hired(userH=user[0], workerIDH=worker[0], orderid=trans[0], status="ONGOING", slot=slot, date=datetime.date(y, m, d))    
                hire.save()
            else:
                hire = hired(userH=user[0], workerIDH=worker[0], orderid=trans[0], status="UPCOMING", slot=slot, date=datetime.date(y, m, d))
                hire.save()
        else:
            hire = hired(userH=user[0], workerIDH=worker[0], orderid=trans[0], status=checkDate(datetime.date(y, m, d)), slot=slot, date=datetime.date(y, m , d))
            hire.save()
        status = hire.status
        response = {
                    "status": "Success",
                    "data" : {
                        "orderID":tid,
                        "slot":slot,
                        "date":date,
                        "status":status,
                        "workerid":wid,
                        "userid":uid
                        }
            
                    }
    else:
        h = hired.objects.filter(orderid=trans[0])
        if len(h)!=0:
            slot = h[0].slot
            date = h[0].date
            wid = h[0].workerIDH
            uid = h[0].userH
            tid = h[0].orderid
            trans = transaction.objects.filter(transID=tid)
            
            if checkDate(datetime.date(y, m, d))=="COMPLETED":
                if checkTime(now)==slot:
                    hire = hired(orderid=trans[0], status="ONGOING")
                    hire.save()
                else:
                    hire = hired(orderid=trans[0], status="COMPLETED")
                    hire.save()
            else:
                hire = hired(orderid=trans[0], status="UPCOMING")
                hire.save()
            status = hire.status
            response = {
                    "status": "Success",
                    "data" : {
                        "orderID":tid.transID,
                        "slot":slot,
                        "date":date,
                        "status":status,
                        "workerid":wid.workerid,
                        "userid":uid.username
                        }
            
                    }
        else:
            response = {
                "status": "Failed",
                "date": "Invalid transaction id, please try again."
            }
    
    return response
        
def saveWorkers(request):
    uid = request.headers.get("token")
    wid = request.headers.get("workerid")
    user = appUser.objects.filter(username=uid)
    worker = workers.objects.filter(workerid=wid)

    if len(user) & len(worker) != 0:
        w = saved(userS=user[0], workerIDS=worker[0])
        w.save()
        response = {
            "status" : "success",
            "data" : {
                "workerid" : worker[0].workerid,
                "usertoken": user[0].username,
                "saved_id": w.savedID,
                "updated_at": w.updated_at
            }
        }
    else:
        response = {
            "status": "failed",
            "data": "Invalid workerid or usertoken"
        }

    return JsonResponse(response, safe=False, status=200)
    
def denial(uid, wid, tid, reason):
    worker = workers.objects.filter(workerid=wid)
    user = appUser.objects.filter(username=uid)
    trans = transaction.objects.filter(transID=tid)


    if len(worker)==0:
        response={
            "status":"Failed",
            "data": "Invalid worker ID"
        }
    elif len(user)==0:
        response={
            "status":"Failed",
            "data": "Invalid user token"
        }
    elif len(trans)==0:
        response={
            "status":"Failed",
            "data": "Invalid transaction ID"
        }
    
    if reason == "Worker not available":
        r = "WORKER DENIED"
    else:
        r = "NOT SATISFACTORY"
    
    deny = dutyDenials(worker=worker[0], user=user[0], transid=trans[0], reason=r)

    response={
        "status":"Success",
        "data": {
            "reason": deny.reason,
            "worker": deny.worker.workerid,
            "user": deny.user.username,
            "transid": deny.transid.transID,
            "timestamp": deny.updated_at
        }
    }
    
    return response
    
def showHistory(uid):
    user = appUser.objects.filter(username=uid)

    if len(user)==0:
        response = {
            "status":"Failure",
            "data":"Invalid user token"
            
            }
    save = saved.objects.filter(userS=user[0])
    res = []
    if len(save)!=0:
        for x in save:
            r = workRating.objects.filter(workerIDR=x.workerIDS)
            rat = []
            if len(r) != 0:
                for y in r:
                    avrat = y.rat_1/4 + y.rat_2/4 + y.rat_3/4 + y.rat_4/4
                    rat.append(avrat)
            else:
                rat = [0]
            
            
            dat = {
                "savedid": x.savedID,
                "workerid": x.workerIDS.workerid,
                "name":x.workerIDS.name,
                "wages":x.workerIDS.wages, 
                "wagesType":x.workerIDS.wagestype,
                "rating": sum(rat)/len(rat),
                "skills": x.workerIDS.skills,
                "location": x.workerIDS.add
                }
            res.append(dat)
    else:
        res = "No saved history found."

    hire = hired.objects.filter(userH=user[0])

    ress = []

    if len(hire)!=0:
        for x in hire:
            r = workRating.objects.filter(workerIDR=x.workerIDH)
            rat = []
            if len(r) != 0:
                for y in r:
                    avrat = y.rat_1/4 + y.rat_2/4 + y.rat_3/4 + y.rat_4/4
                    rat.append(avrat)
            else:
                rat = [0]
            
            
            dat = {
                "savedid": x.hiredID,
                "workerid": x.workerIDH.workerid,
                "name":x.workerIDH.name,
                "wages":x.workerIDH.wages, 
                "wagesType":x.workerIDH.wagestype,
                "rating": sum(rat)/len(rat),
                "skills": x.workerIDH.skills,
                "location": x.workerIDH.add
                }
            ress.append(dat)
    else:
        ress = "No hired history found."
    
    response = {
        "status":"Success",
        "data":{
            "saved":res,
            "hired":ress
        }
    }

    return response
    # return JsonResponse(response, safe=False, status=200)
    

            
