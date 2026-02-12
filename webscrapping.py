import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import smtplib
def getresult(url):
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"}
    response=requests.get(url,headers=headers,verify=False)
    print(f"Server Responds:{response.status_code}")
    soup=BeautifulSoup(response.content,"html.parser")
    price_element=soup.find(class_="a-price-whole")
    title_element=soup.find(id="productTitle")
    if title_element:
        product_title=title_element.get_text().strip()
        print(f"The product name is: {product_title}")
    if price_element:
         price=price_element.get_text().strip()
         clean_price=price.replace(".","").replace(",","")
         current_price=float(price)
         print(f"The price of the product is: {current_price}")
         budget=1000
         if current_price<=budget:
             print("Price is low. Sending email")
             send_email(product_title,current_price,url)

         else:
             print("Price is high we can wait for sale")
    else:
        print("Could not able to find the price may be the product is sold and not avaliable")
    if "Add to Cart" in response.text:
        print("This is also in cart so : You can buy it")
    else:
        print("Not avaliable")
        print(response.text[:100])
def send_email(product_title,current_price,url):
    my_email="supyallukshyadl1@gmail.com"
    my_password="chkg ysvm xhse qjrs "
    receiver_address="supyallukshyadl1@gmail.com"
    message = f"Subject: LOW PRICE ALERT!\n\nHi! The price for {product_title} has dropped to {current_price}.\n\nBuy it here: {url}"
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
         connection.starttls()
         connection.login(user=my_email,password=my_password)
         connection.sendmail(
              from_addr=my_email,
              to_addrs=receiver_address,
              msg=message
         )
         print("EMAIL SENT SUCCESSFULLY!")
         

getresult("https://amzn.in/d/0c5YDIAN")

    