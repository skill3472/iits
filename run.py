#!/usr/bin/env /bin/python
import requests
import urllib.parse
import base64

# Load secret
file = open("secret.txt", "r")
data = file.read().splitlines()
file.close()

# Encode secret
s = f"{data[0]}:{data[1]}"
s_bytes = s.encode('ascii')
b64_bytes = base64.b64encode(s_bytes)
b64_s = b64_bytes.decode('ascii')

# Authorization
headers = {
  "Authorization": f"Basic {b64_s}",
  "Content-Type": "application/x-www-form-urlencoded"
}
data = {
  "grant_type": "client_credentials"
}
r = requests.post('https://accounts.spotify.com/api/token', headers = headers, data = data)
auth = r.json()["access_token"]
print(auth)