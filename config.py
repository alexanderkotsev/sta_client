#!/usr/bin/env python3

STA_ENDPOINT = {'url': 'http://localhost:8080/v1.0/Observations',
                'query': '?$top=1',
                'datastreams': {
                    'ch0': {"@iot.id": 1},
                    'ch1': {"@iot.id": 2},
                    'ch2': {"@iot.id": 3},
                    'ch3': {"@iot.id": 4},
                    'ch4': {"@iot.id": 5},
                    'ch5': {"@iot.id": 6},
                    'ch6': {"@iot.id": 7},
                }
                }

DATABASE = {'db': 'airsenseur.db'}

