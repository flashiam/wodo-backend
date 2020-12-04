from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from django.shortcuts import get_object_or_404
from exotel import Exotel

sid = "specsoidsystems1"
token = "84dd6ad2ca3e6bb2886d0307492526dbcfeae0bd52759bf5"

def custCalls(request):
    client = Exotel(sid,token)
    c = client.call_number('9630961847 ','095-138-86363','0755-4923236')

    return JsonResponse(c)