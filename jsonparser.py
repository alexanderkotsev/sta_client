#!/usr/bin/env python3

import dbparser as db
import config
import json
import datetime
import requests

def json_create(channel):

    json_obj = str(json.dumps({
        "phenomenonTime": utctime,
        "resultTime": utctime,
        "result": obs[1],
        "Datastream": config.STA_ENDPOINT['datastreams'][channel]
    }))
    return json_obj


if hasattr(db, 'new_observations'):
    for e, obs in enumerate(db.new_observations):
        inttime = int((obs)[9]) / 1000
        utctime = datetime.datetime.utcfromtimestamp(inttime).isoformat() + 'Z'
        if obs[3] == 0:
            json_objects = json_create('ch0')
            r = requests.post(config.STA_ENDPOINT['url'], json_objects)
            print("Server status is:", r.status_code, r.reason)
            print(str(json_objects))
            continue
        elif obs[3] == 1:
            json_objects = json_create('ch1')
            r = requests.post(config.STA_ENDPOINT['url'], json_objects)
            print("Server status is:", r.status_code, r.reason)
            print(str(json_objects))
            continue
        elif obs[3] == 2:
            json_objects = json_create('ch2')
            r = requests.post(config.STA_ENDPOINT['url'], json_objects)
            print("Server status is:", r.status_code, r.reason)
            print(str(json_objects))
            continue
        elif obs[3] == 3:
            json_objects = json_create('ch3')
            r = requests.post(config.STA_ENDPOINT['url'], json_objects)
            print("Server status is:", r.status_code, r.reason)
            print(str(json_objects))
            continue
        elif obs[3] == 4:
            json_objects = json_create('ch4')
            r = requests.post(config.STA_ENDPOINT['url'], json_objects)
            print("Server status is:", r.status_code, r.reason)
            print(str(json_objects))
            continue
        elif obs[3] == 5:
            json_objects = json_create('ch5')
            r = requests.post(config.STA_ENDPOINT['url'], json_objects)
            print("Server status is:", r.status_code, r.reason)
            print(str(json_objects))
            continue
        elif obs[3] == 6:
            json_objects = json_create('ch6')
            r = requests.post(config.STA_ENDPOINT['url'], json_objects)
            print("Server status is:", r.status_code, r.reason)
            print(str(json_objects))
            continue
        elif obs[3] == 7:
            json_objects = json_create('ch7')
            r = requests.post(config.STA_ENDPOINT['url'], json_objects)
            print("Server status is:", r.status_code, r.reason)
            print(str(json_objects))
            continue
else:
    print("Nothing to be pushed to the server!")
