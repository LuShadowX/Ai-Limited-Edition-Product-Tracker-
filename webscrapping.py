import requests
def getresult(url):
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"}
    response=requests.get(url,headers=headers)
    print(f"Server says this:{response.status_code}")
    if "Add to Cart" in response.text:
        print("You can buy it")
    else:
        print("Not avaliable")
        print(response.text[:100])
    

getresult("https://amzn.in/d/0c5YDIAN")