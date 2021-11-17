import requests
import json
 
access_token ='MzZhM2ZkMjAtYWU2NS00N2U5LWE3NTgtMmM0YTg2ZGUxOTFmZDhlN2IxNTQtNTRl_P0A1_5bec38e4-205e-4e47-80fa-b272c913bcbf'
url='https://webexapis.com/v1/messages'

message='Hola a ***DEVNET LABS***'
roomId='Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vMTc1NDViOTAtNDRkNS0xMWVjLWFkN2MtYmIwNjI4Yjg5OTBh'

headers ={
    'Authorization':'Bearer {}'.format(access_token),
    'Content-Type':'application/json'
}

params={
    'roomId':roomId,
    'markdown':message
}

resp = requests.post(url,headers=headers,json=params)
print(json.dumps(resp.json(),indent=4))