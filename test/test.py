#*
# Archivo de testeos, dejar vacio!
# *#
import requests
import json
number = "+573213796642"
kato_key = "a65976cc48a83b234e1b7177d0b3840f"
url = "http://apilayer.net/api/validate?access_key="+kato_key+"&number="+number+""
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Origin': 'https://numverify.com/',
    'x-requested-with': 'XMLHttpRequest'
}
r = requests.get(url)
print(r.text)
j = json.loads(r.text)
print("text"+j['country_prefix'])