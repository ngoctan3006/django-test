import requests

reponse = requests.get('http://localhost:8000/drinks/')
print(reponse.json())
