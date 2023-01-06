#!/bin/python
from subprocess import check_output
from json import loads, dumps

print("Loading ip data...\n")
with open('ips.json','r') as file:
    ips=[ip["ip"] for ip in loads(file.read())]

print("Ip data:\n")
for i in ips:
    print(i)

print("\nStarting to ping...\n")
for ip in ips:
    status={"ip":ip,"status":loads(check_output(['mcstatus', ip, "json"]))}

    print(status)
    with open('mc-server-list.json','a') as file:
        file.write(dumps(status)+",\n")

print("\nTa-da!!!")
