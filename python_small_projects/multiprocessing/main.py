import time

def spider_url(url):
    print('spider %s'%url)
    time.sleep(2)


if __name__=="__main__":
    tospider_urls=["https://www.url%d.com"%i for i in range(100)]
    for url in tospider_urls:
        spider_url(url)




