import requests
import json
access_token ='MzZhM2ZkMjAtYWU2NS00N2U5LWE3NTgtMmM0YTg2ZGUxOTFmZDhlN2IxNTQtNTRl_P0A1_5bec38e4-205e-4e47-80fa-b272c913bcbf'
url='https://webexapis.com/v1/rooms'


headers ={
    'Authorization':'Bearer {}'.format(access_token),
    'Content-Type':'application/json'
}
params ={
    'max':'100'
}

resp = requests.get(url,headers=headers,params=params)
print(json.dumps(resp.json(),indent=4))