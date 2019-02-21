#!/usr/bin/env python3

import dbparser as db
import config
import json
import datetime
import requests

if hasattr(db, 'new_observations'):
    for e, obs in enumerate(db.new_observations):
        inttime = int((obs)[9]) / 1000
        utctime = datetime.datetime.utcfromtimestamp(inttime).isoformat() + 'Z'
        json_objects = str(json.dumps({
        "phenomenonTime": utctime,
        "resultTime": utctime,
        "result": obs[2],
        "Datastream": config.STA_ENDPOINT['datastreams']['ch1']
            }))

        r = requests.post(config.ENDPOINT['url'], json_objects)
        print("Data successfully pushed to STA Server ", r.status_code, r.reason)
else:
    print("Nothing to be pushed to the server!")
