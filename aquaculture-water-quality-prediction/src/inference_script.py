import urllib.request
import json
import os
from dotenv import load_dotenv

load_dotenv()

data = {}
body = str.encode(json.dumps(data))

url = os.getenv("ENDPOINT")
api_key = os.getenv("API_KEY")
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + api_key
}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)
    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code:", error.code)
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))
