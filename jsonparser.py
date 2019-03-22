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
    for obs in db.new_observations:
        inttime = int((obs)[9]) / 1000
        utctime = datetime.datetime.utcfromtimestamp(inttime).isoformat() + 'Z'
        json_objects = json_create('ch' + str(obs[3]))
        r = requests.post(config.STA_ENDPOINT['url'], json_objects)
        print("Server status is:", r.status_code, r.reason)
        print(str(json_objects))
else:
    print("Nothing to be pushed to the server!")
