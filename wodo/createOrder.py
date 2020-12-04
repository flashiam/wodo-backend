import razorpay 
from django.http import JsonResponse

def createOrder(request):
    amount = request.headers.get("amount")
    notes = {"Purpose": "Wodo wallet recharge"}
    currency = "INR"

    client = razorpay.Client(auth=("rzp_live_zzSqjt3sPAs0W9", "vXlVCqMBFmDzOadwG7ISn2ae"))

    DATA = {
            "amount":int(amount),
            "currency":currency,
            "notes":notes
            }  
    client.order.create(data=DATA)

    data = client.order.all()

    response = {
        "status":"Success",
        "data": data['items'][0]
    }

    return JsonResponse(response, safe=False, status=200)


