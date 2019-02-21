#!/usr/bin/env python3

import config
import requests
import dateutil.parser

sta_server = requests.get(config.STA_ENDPOINT['url'] + config.STA_ENDPOINT['query'])

try:
    r = requests.get(config.STA_ENDPOINT['url'])
    r.raise_for_status()

except requests.exceptions.HTTPError as errh:
    print("Http Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("OOps: Something Else", err)


resp_dict = dict(sta_server.json()) #Converts the JSON response to Python dictionary

json_value = str(resp_dict['value'])

date_str = json_value.split("'")[23] #Gets the resultTime timestamp from the values property

date_parsed = dateutil.parser.parse(date_str) #Parses the date
utc_time = int(date_parsed.timestamp() * 1000)
