import requests
from bs4 import BeautifulSoup
import module


URL="https://www.amazon.in/Redmi-9A-Midnight-2GB-32GB/dp/B08697N43G/ref=sr_1_1?adgrpid=64822842374&ext"
r = requests.get(URL)

soup=BeautifulSoup(r.content,'html.parser')
print(soup.prettify())
print(soup.title())
a=module.mobileinfo()
a.process()







