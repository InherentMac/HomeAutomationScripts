import requests
import json

##FW CONTROL
meraki_api = "https://api.meraki.com/api/v1/devices/"FW_SN"/clients"
#meraki_api_token = "Nice try"
headers = {
    "X-Cisco-Meraki-API-Key": "Nice try"
}
#params = {
#    "timespan": "30"
#}

##LIGHT CONTROL
philips_hub_api = "http://1.2.3.4/api/"API_key"/groups/0/action"
lights_off = {"on":False}
lights_on = {"on":True}
##FW CLIENT LIST REQUEST
meraki_FW_response = requests.get(meraki_api, headers=headers) ##params=params
##Meraki API DEBUGGING
print(meraki_FW_response.status_code)
print(meraki_FW_response.json())


##CLIENT SEARCH
device_list = meraki_FW_response.json()
found = 0
for i in device_list:
    if i["description"] == "OnePlus 5T":
        ##DEVICE LOCATED
        found = found + 1
        print("located")
    else:
        ##DEVICE NOT CONNECTED TO WIFI
        print("searching...")

##Light control on Mac's presence
if found > 0:
    hue_response = requests.put(philips_hub_api, json=lights_on)
else:
    hue_response = requests.put(philips_hub_api, json=lights_off)
