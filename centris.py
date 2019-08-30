from bs4 import BeautifulSoup
from requests import Session

session = Session()

res = session.get('https://www.centris.ca/en/properties~for-sale')

bs = BeautifulSoup(res.text,features="html.parser")


span = bs.find("span", id="numberOfResults")
nb_of_results = int(span.text)

print(nb_of_results)
response = session.post('https://www.centris.ca/Mvc/Property/GetInscriptions',data={"startPosition":0})

if not response.ok:
    response.raise_for_status()

data = response.json()

bs = BeautifulSoup(data['d']['Result']['html'],features="html.parser")

for ref in bs.find_all('a',{'class':'btn a-more-detail'}):
    print(ref['href'])
