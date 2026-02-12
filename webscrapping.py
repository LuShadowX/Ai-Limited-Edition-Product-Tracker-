import requests
from bs4 import BeautifulSoup
def getresult(url):
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"}
    response=requests.get(url,headers=headers)
    print(f"Server Responds:{response.status_code}")
    soup=BeautifulSoup(response.content,"html.parser")
    title_element=soup.find(id="productTitle")
    if title_element:
        product_title=title_element.get_text().strip()
        print(f"The product name is: {product_title}")
    if "Add to Cart" in response.text:
        print("You can buy it")
    else:
        print("Not avaliable")
        print(response.text[:100])
    

getresult("https://amzn.in/d/0c5YDIAN")