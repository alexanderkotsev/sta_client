#!/usr/bin/env python3

STA_ENDPOINT = {'url': 'http://localhost:8080/v1.0/Observations',
                'query': '?$top=1',
                'datastreams': {
                    'ch0': {"@iot.id": 2},
                    'ch1': {},
                    'ch2': {},
                    'ch3': {},
                    'ch4': {},
                    'ch5': {},
                    'ch6': {},
                }
                }

DATABASE = {'db': 'airsenseur.db'}

