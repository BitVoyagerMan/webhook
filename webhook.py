import requests
import json
webhook_url = "https://webhook.site/729697dc-7bfe-4f16-b9e2-6755c7d00e65"
data = {'name' : 'DevOps Journey', 'content': 'nothing'}

r = requests.post(webhook_url, data = json.dumps(data), headers={'Content-Type' : 'application/json'})