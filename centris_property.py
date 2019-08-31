# import requests
# res = requests.get('https://www.centris.ca/en/houses~for-sale~grenville-sur-la-rouge/20045495?view=Summary')
#
# with open('test.html','w') as f:
#     f.write(res.text)

from bs4 import BeautifulSoup


class CentrisProperty(object):


    def __init__(self,html):
        self.bs = BeautifulSoup(html,features='html.parser')


    @property
    def price(self):
        return self.bs.find('span',{'id':'BuyPrice'})['content']

    @property
    def property_type(self):
        return self.bs.find('span',{'data-id':'PageTitle'}).text



with open('test.html','r') as f:
    html = f.read()


cp = CentrisProperty(html)

print(cp.property_type)


from requests import Session

session = Session()

res = session.get('https://passerelle.centris.ca/redirect.aspx?&CodeDest=VIACAPITALE&NoMLS=14318834&Lang=E&source=centris.ca')

print(res.text)







