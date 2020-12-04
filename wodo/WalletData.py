from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from wodo.models import transaction, appUser
import json
import math

def CoinsCon(val):
	cval = 0.50
	coins = val/cval
	return coins	

def checkBal(uid):
	
	bal = WalletBal(uid)
	bal = bal*0.50

	if bal>2:
		Status = "Success"
	else:
		Status = "Failed"
	
	return Status

def WalletBal(uid):
	trans = transaction.objects.filter(userT=uid)
	amount = []
	for x in trans:
		if x.transType == "DEBIT":
			amount.append(-float(x.amount))
		else:
			amount.append(float(x.amount))
	
	bal = sum(amount)
	return CoinsCon(bal)

def history(uid):
	proceeds = []
	trans = transaction.objects.filter(userT=uid)
	for z in trans:
		 tid = z.transID
		 pur = z.purpose
		 Type = z.transType
		 ts = z.timestamp
		 coins = CoinsCon(float(z.amount))
		 dat = {"transID": tid, "purpose": pur, "type": Type, "Timestamp": ts, "Coins": coins}
		 proceeds.append(dat)
	proc = proceeds
	return proc
	
def AddMoney(uid, amt, pur):
	user = appUser.objects.filter(username="shiva12")
	tr=0
	if pur == "ADD MONEY":
		c = transaction.objects.filter(purpose=pur, userT=user[0])
		cc = str(len(c)+1)
		transID = pur[0]+pur[1]+pur[2]+cc.zfill(5)
		
	elif pur == "REFERRAL":
		c = transaction.objects.filter(purpose=pur, userT=user[0])
		cc = str(len(c)+1)
		transID = pur[0]+pur[1]+pur[2]+cc.zfill(5)
	elif pur == "NEW USER":
		c = transaction.objects.filter(purpose=pur, userT=user[0])
		cc = str(len(c)+1)
		transID = pur[0]+pur[1]+pur[2]+cc.zfill(5)
	else:
		c = transaction.objects.filter(purpose=pur, userT=user[0])
		cc = str(len(c)+1)
		transID = pur+cc.zfill(5)
	
	o = str(len(transaction.objects.all())+1)
	orderID = o.zfill(8)
	trans = transaction(userT=user[0], amount=amt, orderID=orderID, transID=transID, transType="CREDIT", purpose=pur)
	trans.save()
	tr = trans
	if tr !=0:
		
		bal = WalletBal(uid)
		his = history(uid)
	
		response = {
		    "Transaction": {
				"orderID": tr.transID,
				"amount": tr.amount,
				"date": tr.timestamp,
				"transType": tr.transType,
			},
		    "Status": "Success",
			"Balance": bal,
			"History": his
			}
	else:
		response = {
			"Transaction": {
				"orderID": tr.transID,
				"amount": tr.amount,
				"date": tr.timestamp,
				"transType": tr.transType,
			},
			"Status": "Failed",
			"Balance": bal,
			"History": his
			}
	
	return response
		
def DedMoney(uid, amt, pur):
	user = appUser.objects.filter(username=uid)
	tr = 0
	if pur == "HIRING":
		c = transaction.objects.filter(purpose=pur, userT=user[0])
		cc = str(len(c)+1)
		transID = pur[0]+pur[1]+pur[2]+cc.zfill(5)
		
	else:
		c = transaction.objects.filter(purpose=pur, userT=user[0])
		cc = str(len(c)+1)
		transID = pur[0].pur[1].pur[2]+cc.zfill(5)
	
	o = str(len(transaction.objects.all())+1)
	orderID = o.zfill(8)
	trans = transaction(userT=user[0], amount=amt, orderID=orderID, transID=transID, transType="DEBIT", purpose=pur)
	trans.save()
	tr = trans
	bal = WalletBal(uid)
	his = history(uid)
	if tr != 0:
		response = {
		    "Transaction": {
				"orderID": tr.transID,
				"amount": tr.amount,
				"date": tr.timestamp,
				"transType": tr.transType,
			},
		    "Status": "Success",
			"Balance": bal,
			"History": his
			}
	else:
		response = {
			"Transaction": {
				"orderID": tr.transID,
				"amount": tr.amount,
				"date": tr.timestamp,
				"transType": tr.transType,
			},
			"Status": "Failed",
			"Balance": bal,
			"History": his
			}
	
	return response
	         



