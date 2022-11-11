# This example requires the 'message_content' intent.

import requests
import check


if check.check_func() == '!!SOME LINKS GET ERROR!!':
    file = {
    'file': open('Report.txt', 'rb')
    }   
else:
    file = None



payload = {
    "content":check.check_func()
}

header = {
    'authorization': 'NDYyOTE4MzQ4MDk1NjE5MDcy.GtPeNx.-Qxj9gFXH_O7SJiqN7Opjtf1mOoqVdNI8IPaz0'
}

r = requests.post('https://discord.com/api/v9/channels/1038699651269939240/messages', data=payload, headers=header, files=file)
print(check.check_func())

