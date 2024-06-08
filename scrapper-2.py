import urllib.request, urllib.parse, urllib.error
from urllib.request import Request
from bs4 import BeautifulSoup

from urllib.parse import urlparse,ParseResult,quote

url = input('Введіть URL сторінки, з якої потрібно почати скрапінг:  ')
if len(url) < 1:
    url = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops'


number_of_pages = int(input('Скільки сторінок потрібно спарсити: '))

number_of_pages+=1

# number_of_pages =21    

x = 1
laptop_number=1
while x<= number_of_pages:
    url = urlparse(url)
    url = ParseResult(url.scheme,url.netloc.encode('idna').decode('ascii'),quote(url.path),url.params,url.query,url.fragment).geturl()
    request_site = Request(url, headers={"User-Agent": " Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.49 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"})
    uh = urllib.request.urlopen(request_site).read()
    
    soup = BeautifulSoup(uh, 'html.parser')
   
    for a in soup.find_all("a", {"class": "title"}):
        product_url_without_domain = a.get('href')
        product_url= 'https://webscraper.io'+product_url_without_domain
        product_url = urlparse(product_url)
        product_url = ParseResult(product_url.scheme,product_url.netloc.encode('idna').decode('ascii'),quote(product_url.path),product_url.params,product_url.query,product_url.fragment).geturl()
        request_site = Request(product_url, headers={"User-Agent": " Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.49 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"})
        uh = urllib.request.urlopen(request_site).read()
    
        product_soup = BeautifulSoup(uh, 'html.parser')

        title_html= product_soup.find("h4", {"class": "title card-title"})
        title=title_html.get_text()

        price_html = product_soup.find("h4", {"class": "price float-end pull-right"})
        price = price_html.get_text()


        description_html = product_soup.find("p", {"class": "description card-text"})
        description = description_html.get_text()

        

        print(f'Номер ноутбуку: {laptop_number}')
        print(f'Назва ноутбуку: {title}')
        print(f'Ціна: {price}')
        print(f'Опис: {description}')

        laptop_number = laptop_number + 1
        print('============================================')
        
 
    x+=1
    url = f'https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={x}'
