#!/usr/bin/env python

"""Set servo angle."""

import os
import json
import requests

def get_env(key, type_=int):
    'Return the value of the namespaced Farmware input variable.'
    return type_(os.environ['{}_{}'.format(farmware_name, key)])

def set_servo_angle(pin, angle):
    'Wrap the data in a `set_servo_angle` Celery Script command to send it.'
    return {
        "kind": "set_servo_angle",
        "args": {"pin_number": pin, "pin_value": angle}}

def post(wrapped_data):
    'Send the Celery Script command.'
    headers = {
        'Authorization': 'bearer {}'.format(os.environ['FARMWARE_TOKEN']),
        'content-type': "application/json"}
    payload = json.dumps(wrapped_data)
    requests.post(os.environ['FARMWARE_URL'] + 'api/v1/celery_script',
                  data=payload, headers=headers)

if __name__ == "__main__":
    farmware_name = 'set_servo_angle'
    post(set_servo_angle(get_env('pin_number'), get_env('servo_angle')))
