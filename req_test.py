from requests import Session

session = Session()

session.head('https://www.centris.ca/en/properties~for-sale')

response = session.post('https://www.centris.ca/Mvc/Property/GetInscriptions',data={"startPosition":0})


data = response.json()

print(data['d']['Result']['html'])


