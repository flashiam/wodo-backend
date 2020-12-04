from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from urllib.parse import unquote_plus
from wodo.models import hired
import json
import math

def getContact(request):
    # callsid = request.query_params['CallSid']
    # caller = request.query_params['CallFrom']
    # exophone = request.query_params['CallTo']
    # direction = request.query_params['Direction']
    # created = request.query_params['Created']
    # started = request.query_params['StartTime']
    # time = request.query_params['CurrentTime']
    # caller1 = request.query_params['From']
    data = request.GET
    callsid = data['CallSid']
    caller = data['CallFrom']
    exophone = data['CallTo']
    direction = data['Direction']
    created = data['Created']
    started = data['StartTime']
    time = data['CurrentTime']
    caller1 = data['From']
    

    response = {
        "caller": caller,
        "callto": exophone
    }

    # data = request.GET.urlencode()
    # data = request.META['QUERY_STRING']
    # data = request.GET
    return JsonResponse(response, safe=False, status=200)
    # data = unquote_plus(data)
    # data = json.loads(data)
    # c = data['contact']
#     response = {
#         {
#        "fetch_after_attempt":false,
#        "destination": {
#             "numbers":[]
#        },
#       "outgoing_phone_number":"+918047115777",
#       "record": true,
#       "recording_channels":"dual",
#       "max_ringing_duration":45,
#       "max_conversation_duration":3600,
#       "music_on_hold": {
#            "type":"operator_tone"
#       },
#       "start_call_playback": {
#            "type":"text",
#            "value":"This text would be spoken out to the callee"
#       }
# }
#     }
#     return JsonResponse(response, safe=False, status=200)
     
