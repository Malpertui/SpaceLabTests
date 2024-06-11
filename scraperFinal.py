import urllib.request, urllib.parse, urllib.error
from urllib.request import Request
from bs4 import BeautifulSoup

# 1. У цій функції я вирішив зробити два параметри: URL (url), де треба почати 
# скрапінг, і кількість сторінок (number_of_pages) з прев’ю товарів, які 
# потрібно просканувати. Думаю, що можна зробити без number_of_pages, 
# але часу не вистачило. Зробив, як звик. Також одразу додав дефолтні аргументи.
# Начебто не суперечить умові, і можна без проблем додати свої аргементи.
# 2. Якщо коротко, працює все так: парсер заходить на першу сторінку, знаходить 
# усі посилання з атрибутами class="title", переходить за цими посиланнями і 
# збирає інформацію: назву ноутбуку, ціну і опис. Я ще від себе для зручності 
# додав номер. Коли посилання на сторінці закінчуються, парсер переходить на 
# іншу сторінку з прев’ю. І так до самого кінця. Спочатку я прописав, щоб парсер
# сканував по 6 посилань на кожній сторінці, але (сюрприз-сюрприз!) на останній
#  сторінці посилань не 6. Довелося трохи переробити код.
# 3. В якості User-Agent я вибрав мобільного павука (Android 6.0.1). Мій 
# невеликий досвід з парсерами підказує, що так працює краще 
# (менше блокувань зі сторони сервера). 
# 4. Також я додав оцей код 
# (url.scheme,url.netloc.encode('idna').decode('ascii')…) на випадок, якщо 
# будуть URL кирилицею. Це щоб перевести їх на латиницю. 
# 5. Спочатку я хотів спарсити просто інформацію з прев’ю (не переходити на 
# сторінки товарів). Але виявилося, що уже на третій сторінці навіть назви 
# ноутбуків не повні. Так точно не підійде. Доопрацював. 



from urllib.parse import urlparse,ParseResult,quote
def get_laptos(url='https://webscraper.io/test-sites/e-commerce/static/computers/laptops', number_of_pages=20):
    number_of_pages+=1
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


get_laptos()

