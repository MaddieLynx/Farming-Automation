import os
import requests
import json

headers = {
  'Authorization': 'bearer {}'.format(os.environ['FARMWARE_TOKEN']),
  'content-type': "application/json"}
response = requests.post(os.environ['FARMWARE_URL'] + '/api/v1/bot/state',
              headers=headers)
bot_state = response.json()

position_x = response.json()['location_data']['position']['x']
pin_13_value = response.json()['pins']['13']['value']
