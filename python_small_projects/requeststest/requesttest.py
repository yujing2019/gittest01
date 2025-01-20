import requests
url="https://www.google.com/"
r=requests.get(url)
print(r.text)
while True:
    url="https://www.google.com/"
    r = requests.get(url)
    if r.status_code !=200:
        raise Exception("error")
    print("running success")
    import time
    time.sleep(2)

