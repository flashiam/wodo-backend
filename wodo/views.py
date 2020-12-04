# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from wodo.models import workers, workRating, filterCache, appUser
from wodo.WalletData import *
from wodo.hirings import *
import json
import math
import statistics
from geopy.distance import geodesic
import re
# Create your views here.

def jsonMaker(a, b):
    output = {a:b}
    return output

def Convert(string): 
    list1=[] 
    list1[:0]=string 
    return list1 

def showFilter(request):
    token = request.headers.get("token")
    city = request.headers.get("city")
    lats = request.headers.get("lat")
    longs = request.headers.get("long")
    skill = request.headers.get("skills")
    wage = request.headers.get("wages")

    s = json.dumps(skill)
    s = s.split(",")

    s[0] = s[0][1:]
    s[len(s)-1] = s[len(s)-1][:-1]

    user = appUser.objects.filter(username=token)

    if len(user) is 0:
        response={
            "status":"Failed",
            "code":"Invalid Token"
        }
        return JsonResponse(response, safe=False)

    

    lat2 = lats
    long2 = longs
    location = {
        "lats":lats,
        "long":longs
        }
    o = []
    
    for x in range(len(s)):
        doo = {
            "id": x,
            "skill":s[x]
        }
        o.append(doo)
    
    jobs = o
    fil = filterCache(userF=user[0], location=location, wages=float(wage), jobs=jobs, city=city)
    fil.save()
   
    work = workers.objects.filter(city=city)
    fins = []
    
    for i in s:
        data = []
        
        for w in work:
            if i in json.dumps(w.skills):
                lat1 = float(w.coor["Lat"])
                long1 = float(w.coor["Long"])
                coor1 = (lat1, long1)
                coor2 = (lat2, long2)
                dist = geodesic(coor1, coor2).km
    
                if float(dist) <= w.distance:
                    
                    r = workRating.objects.filter(workerIDR=w.workerid)
                    rat = []
                    if len(r) != 0:
                        for y in r:
                            avrat = y.rat_1/4 + y.rat_2/4 + y.rat_3/4 + y.rat_4/4
                            rat.append(avrat)
                    else:
                        rat = [0]
                    
                    if float(wage) >= float(w.wages):
                        budget = True
                    else:
                        budget = False
                    
                    
                    data.append({"workerid": w.workerid, "name": w.name, "wages": w.wages, "wagestype": w.wagestype, "rating": statistics.mean(rat), "Location": w.add, "status": "Recommended", "distance": round(float(dist), 1), "budget": budget, "coor": w.coor, "verified": w.verified})
                    
                    #data[w.name] = [w.workerid, w.name, w.wages, w.wagestype, statistics.mean(rat), w.add, "Recommended", round(float(dist), 1), budget, w.coor]
                else:
            
                    r = workRating.objects.filter(workerIDR=w.workerid)
                    rat = []
                    if len(r) != 0:
                        for y in r:
                            avrat = y.rat_1/4 + y.rat_2/4 + y.rat_3/4 + y.rat_4/4
                            rat.append(avrat)
                    else:
                        rat = [0]
                
                    if float(wage) >= float(w.wages):
                        budget = True
                    else:
                        budget = False
                    
                    milage = 5
                    extra = (float(dist)-w.distance)*milage
                    wages = round(w.wages + extra ,1)

                    data.append({"workerid": w.workerid, "name": w.name, "wages": wages, "wagestype": w.wagestype, "rating": statistics.mean(rat), "Location": w.add, "status": "Suggested", "distance": round(float(dist), 1), "budget": budget, "coor": w.coor, "verified": w.verified})
                
                #data[w.name] = [w.workerid, w.name, w.wages, w.wagestype, statistics.mean(rat), w.add, "Suggested", round(float(dist), 1), budget, w.coor]
            
        fins.append(data)

    f = dict(zip(s, fins))    

    return JsonResponse(f, safe=False, status=200)

def allWorkers(request):
    city = request.headers.get("city")
    lats = request.headers.get("lat")
    longs = request.headers.get("long")

    work = workers.objects.filter(city=city)

    lat2 = lats
    long2 = longs
   
    data = []
    fins = []
    for w in work:
        
        lat1 = float(w.coor["Lat"])
        long1 = float(w.coor["Long"])
        coor1 = (lat1, long1)
        coor2 = (lat2, long2)
        dist = geodesic(coor1, coor2).km

        if float(dist) <= w.distance:
            
            r = workRating.objects.filter(workerIDR=w.workerid)
            rat = []
            if len(r) != 0:
                for y in r:
                    avrat = y.rat_1/4 + y.rat_2/4 + y.rat_3/4 + y.rat_4/4
                    rat.append(avrat)
            else:
                rat = [0]
            
            
            
            
            data.append({"workerid": w.workerid, "name": w.name, "wages": w.wages, "wagestype": w.wagestype, "rating": statistics.mean(rat), "Location": w.add, "status": "Recommended", "distance": round(float(dist), 1), "coor": w.coor, "skill": [w.skills['s1'], w.skills['s2'], w.skills['s3']], "verified": w.verified})
            
            #data[w.name] = [w.workerid, w.name, w.wages, w.wagestype, statistics.mean(rat), w.add, "Recommended", round(float(dist), 1), budget, w.coor]
        else:
        
            r = workRating.objects.filter(workerIDR=w.workerid)
            rat = []
            if len(r) != 0:
                for y in r:
                    avrat = y.rat_1/4 + y.rat_2/4 + y.rat_3/4 + y.rat_4/4
                    rat.append(avrat)
            else:
                rat = [0]
            
           
            
            milage = 5
            extra = (float(dist)-w.distance)*milage
            wages = round(w.wages + extra ,1)

            data.append({"workerid": w.workerid, "name": w.name, "wages": wages, "wagestype": w.wagestype, "rating": statistics.mean(rat), "Location": w.add, "status": "Suggested", "distance": round(float(dist), 1), "coor": w.coor, "skill": [w.skills['s1'], w.skills['s2'], w.skills['s3']], "verified": w.verified})
            
            #data[w.name] = [w.workerid, w.name, w.wages, w.wagestype, statistics.mean(rat), w.add, "Suggested", round(float(dist), 1), budget, w.coor]
        
        # fins.append(data)
    response = {
        "status" : "success",
        "data" : data
    }
     

    return JsonResponse(response, safe=False, status=200)

def skillList(request):
    city = request.headers.get("city")
    skills = []
    vals = []
    w = workers.objects.filter(city=city)

    for x in w:
        skills.append(x.skills)

    for x in skills:
        if x["s1"]!="Skill":
            vals.append(x["s1"])
        elif x["s2"]!="Skill":
            vals.append(x["s2"])
        elif x["s3"]!="Skill":
            vals.append(x["s3"])
        else:
            vals.append("404")

    val = list(set(vals))
    
    ids = []
    for i in range(len(val)):
        ids.append(i)


    fins = []
    for x in range(len(ids)):
        data  = {"id": ids[x],
                "skill": val[x]
                }   
        fins.append(data)
    
    response = {
        "status" : "success",
        "skills" : fins
    }

    
    


    
    
    # val = dict(zip(ids, val))  
    # val = json.dumps(val)



    return JsonResponse(response, safe=False, status=200)

def filterData(request):
    token = request.headers.get("token")
    

    fdata = filterCache.objects.filter(userF=token)

    if len(fdata)!=0:
        
        data = {
            "loc":fdata[0].location,
            "budget":fdata[0].wages,
            "skill":fdata[0].jobs,
            "city":fdata[0].city,
            "add":fdata[0].add,
        }

        response = {
            "status":"success",
            "data": data
        }
    else:
        response = {    
            "status":"Failed",
            "data":"Maa Chudao Tum"
        }

    return JsonResponse(response, safe=False, status=200)    

def testJson(request):
    token = request.headers.get("token")

    response = {
        "status" : "success",
        "skills" : [
            {"id": 1,
            "skill": "Plumber"},
            {"id": 2,
            "skill": "Electrician"}
        ]
    }

    return JsonResponse(response, status=200)

def firstCall(request):
    token = request.headers.get("token")

    user = appUser.objects.filter(username=token)
    
    if len(user) is 0:
        response={
            "status":"Failed",
            "data":"Invalid Token"
        }
        return JsonResponse(response, safe=False)


    fdata = filterCache.objects.filter(userF=user[0])

    if len(fdata)!=0:
        
        response = {
            "status": "success",
            "data": [{
                "location":{"lat": fdata[0].location['lats'],
                            "long": fdata[0].location['long']},
                "city":fdata[0].city,
                "skills":fdata[0].jobs,
                "wages":fdata[0].wages,
                "address":fdata[0].add
            
            }]
        }
    
    else:

        response = {
            "status": "failed",
            "data": "No cache data available for this user"
        }

    return JsonResponse(response, safe=False)

def checkBalance(request):
    token = request.headers.get("token")
    response = {
        "status": "Success",
        "data" : checkBal(token)
    }
    return JsonResponse(response, safe=False, status=200)

def WalletBalance(request):
    token = request.headers.get("token")
    response = {
        "status": "Success",
        "data": WalletBal(token)
    }
    return JsonResponse(response, safe=False, status=200)

def WalletParas(request):
    token = request.headers.get("token")
    response = {
        "status": "Success",
        "data": history(token)
    }

    return JsonResponse(response, safe=False, status=200)

def AddWodoMoney(request):
    token = request.headers.get("token")
    amount = request.headers.get("amount")
    purpose = "ADD MONEY"

    response ={
        "status": "Success",
        "data": AddMoney(token, amount, purpose)
    }
    return JsonResponse(response, safe=False, status=200)

def DedWodoMoney(request):
    token = request.headers.get("token")
    amount = request.headers.get("amount")
    purpose = "HIRING"

    response = {
        "status": "Success",
        "data": DedMoney(token, amount, purpose)
    }
    return JsonResponse(response, safe=False, status=200)

def showProfile(request):
    wid = request.headers.get("workerid")
    token = request.headers.get("token")

    worker = workers.objects.filter(workerid=wid)
     
def showRat(request):
    wid = request.headers.get("workerid")
    rats = workRating.objects.filter(workerIDR=wid)
    data = []
    for x in rats:
        res = {
            "ratid": x.ratingID,
            "rat1": x.rat_1,
            "rat2": x.rat_2,
            "rat3": x.rat_3,
            "rat4": x.rat_4,
            "comment": x.comment,
            "user": x.userR.name,
            "date": x.hiredOn
        }
        data.append(res)

    response = {
        "status":"success",
        "data": data
    }
    return JsonResponse(response, safe=False, status=200)
    
def hireWorker(request):

    wid = request.headers.get("workerid")
    uid = request.headers.get("token")
    date = request.headers.get("daatee")
    slot = request.headers.get("slot")
    tid = request.headers.get("transid")

    h = hire(wid, uid, tid, slot, date)

    response = {
        "status": "Success",
        "data": h
    }

    return JsonResponse(response, safe=False, status=200)

def dutyDenial(request):
    uid = request.headers.get("token")
    wid = request.headers.get("workerid")
    tid = request.headers.get("transid")
    rea = request.headers.get("reason")

    dd = denial(uid, wid, tid, rea)

    response = {
        "status": "Success",
        "data": dd
    }

    return JsonResponse(response, safe=False, status=200)

def historyWatch(request):
    uid = request.headers.get("token")

    if uid:
        data = showHistory(uid)
    else:
        data = "Something went wrong."
    
    response = {
        "status":"Success",
        "data":data
    }

    return JsonResponse(response, safe=False, status=200)
