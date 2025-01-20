import time
import multiprocess as mp

def spider_url(url):
    print('spider %s'%url)
    time.sleep(2)


if __name__=="__main__":
    tospider_urls=["https://www.url%d.com"%i for i in range(100)]
    with mp.Pool() as pool:
        pool.map(spider_url,tospider_urls)






