import requests
import sqlalchemy

r = requests.get("https://www.python.org/")
print(r.status_code)
print(r.text)

for x in range(5):
    print(x)