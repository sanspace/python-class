import requests
from bs4 import BeautifulSoup
from urlparse import urlparse


url = 'http://cardnival.in/'
base = '{uri.scheme}://{uri.netloc}/'.format(uri=urlparse(url))

response = requests.get(url)
soup = BeautifulSoup(response.content, "html5lib")

contact_link = soup.find("a", string="Contact us").get('href')

if contact_link:
    contact_url = base + contact_link
    response = requests.get(contact_url)
    soup = BeautifulSoup(response.content, "html5lib")
    emails = {a["href"][7:] for a in soup.select('a[href^=mailto:]')}
    print emails
        
    
    


