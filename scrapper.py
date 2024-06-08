from collections import Counter
import urllib.request, urllib.parse, urllib.error
import ssl
from urllib import request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

from urllib.parse import urlparse,ParseResult,quote

url = input('Введіть URL сторінки, з якої потрібно почати скрапінг:  ')
if len(url) < 1:
    url = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops'

# url = urlparse(url)
# url = ParseResult(url.scheme,url.netloc.encode('idna').decode('ascii'),quote(url.path),url.params,url.query,url.fragment).geturl()
# print(url)

# url2 = urllib.parse.quote(url)
# request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
# request_site = Request(url, headers={"User-Agent": " Chrome/120.0.0.0"})
# request_site = Request(url, headers={"User-Agent": " Safari/537.36"})

# number_of_pages = int(input('Скільки сторінок потрібно спарсити: '))

number_of_pages =21
    




x = 1

while x<= number_of_pages:
    url = urlparse(url)
    url = ParseResult(url.scheme,url.netloc.encode('idna').decode('ascii'),quote(url.path),url.params,url.query,url.fragment).geturl()
    request_site = Request(url, headers={"User-Agent": " Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.49 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"})
    uh = urllib.request.urlopen(request_site).read()
    
    soup = BeautifulSoup(uh, 'html.parser')

    

    # y = 0
    # while y<= 6:
    # title_list=soup.find("a", {"class": "title"})
    # print(title.get_text())
    # price = soup.find("h4", {"class": "price float-end card-title pull-right"})
    # print(price.get_text())
    # print('============================================')
    #     # y+=1

    title_list =[]
    for a in soup.find_all("a", {"class": "title"}):
        # print(laptop_number)
        title=a.get_text()
        title_list.append(title)
        # print('============================================')
    
    print(title_list)

    price_list = []
    for h4 in soup.find_all("h4", {"class": "price float-end card-title pull-right"}):   
        price=h4.get_text()
        price_list.append(price)
    
    print(price_list)

    desc_list =[]
    for desc in soup.find_all("p", {"class": "description card-text"}):   
        description = desc.get_text()
        desc_list.append(description)

    print(desc_list)
    
    laptop_number=1
    number_of_laptops_page = len(soup.find_all("div", {"class": "product-wrapper card-body"}))
    for i in range(number_of_laptops_page):
        print(f'Номер ноутбука на сторінці {x}: {laptop_number}')
        print(f'Назва: {title_list[i]}')
        print(f'Ціна: {price_list[i]}')
        print(f'Опис: {desc_list[i]}')
        print('============================================')
        laptop_number+=1
    
    x+=1
    url = f'https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={x}'

    




    # for a in soup.find_all("a", {"class": "title"}):
    #     print(laptop_number)
    #     print(a.get_text())
    #     print('============================================')
        
        
    # for price in soup.find_all("h4", {"class": "price float-end card-title pull-right"}):   
    #     print(price.get_text())
        

    # for desc in soup.find_all("p", {"class": "description card-text"}):   
    #     print(desc.get_text())   
        
    # laptop_number+=1
    

    # x+=1