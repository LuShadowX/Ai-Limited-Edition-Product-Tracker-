import requests
def getresult(url):
    response=requests.get(url)
    print(f"Server says this:{response.status_code}")
    if "Add to Cart" in response.text:
        print("You can buy it")
    else:
        print("Not avaliable")
    

getresult("https://amzn.in/d/0c5YDIAN")