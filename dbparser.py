#!/usr/bin/env python3

import sqlite3
import starequests

ase_conn = sqlite3.connect('airsenseur.db')
cursor = ase_conn.cursor()
cursor.execute("SELECT * FROM measures ORDER BY collectedts DESC LIMIT 1")
results = cursor.fetchone()
timestamp_int = (int(results[9]))

if starequests.utc_time < timestamp_int:
    str_select = ('SELECT * FROM measures WHERE collectedts > ' + str(starequests.utc_time))
    cursor.execute(str_select)
    new_observations = cursor.fetchall()
    nrows_new = len(new_observations)
    print("Number of obsertvations to be pushed:", nrows_new)
    ase_conn.close()
else:
    print('No newer data is available!')
