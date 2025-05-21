# Author: Mohammad Reza Arani

import requests
from bs4 import BeautifulSoup

url = "https://ofarm.ir/"

response = requests.get(url)
response.encoding = 'utf-8'  

if response.status_code == 200:
  
    soup = BeautifulSoup(response.text, 'html.parser')

    page_title = soup.title.string.strip() if soup.title else "No title found"
    print("Page Title:", page_title)

    product_titles = soup.find_all(class_="woocommerce-loop-product__title")
    print("\nProduct Titles:")
    for product in product_titles:
        print("-", product.get_text(strip=True))
    
    print("\nProduct Images:")
    for img in soup.find_all("img"):
        src = img.get("src") or img.get("data-src") or img.get("srcset")
        if src:
            print("-", src)
else:
    print("Failed to fetch the website. Status code:", response.status_code)
