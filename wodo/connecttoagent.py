import requests
from pprint import pprint

sid         = 'specsoidsystems1'                                           
key         = '0a188712b647ae8a2312278019341b396e8e27c22aa92916'                                           
token       = '84dd6ad2ca3e6bb2886d0307492526dbcfeae0bd52759bf5'         
smsurl      = 'https://api.exotel.in/v1/Accounts/<exotel_sid>/Sms/send.json'
callurl     = 'https://api.exotel.in/v1/Accounts/specsoidsystems1/Calls/connect.json'
url         = "http://my.exotel.com/<exotel_sid>/exoml/start_voice/<flow_id>", 



def connect_customer_to_agent(
        sid,
        token,
        agent_no,
        customer_no,
        callerid,
        timelimit=None,
        timeout=None,
        calltype = 'trans'
    ):
    return requests.post(
        callurl,
        auth = (sid, token),
        data = {
            'From': from_no,
            'To'  : to,
          
        }
    )

if __name__ == '__main__':
    r = connect_customer_to_agent(
        sid,
        token,
        agent_no    = "your-agent-number",
        customer_no = "your-customer-number",
        callerid    = "<Your-Exotel-virtual-number>",
        timelimit   = "<time-in-seconds>",  
        timeout     = "<time-in-seconds>",  
        calltype    = "trans"  
    )
    print (r.status_code)
    pprint(r.json())
