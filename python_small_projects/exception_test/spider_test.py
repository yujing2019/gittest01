"""
simulate python spider
"""
urls=["http://url1","http://url2","http://url3","http://url4"]


def spider_url(url):
    """
    scratch a single url

    :param url:
    :return:
    """
    if "url2" in url:
        raise Exception ("url return none :")
    return url+":success data"

def spider_urls(urls):
    """

    scratch multiple urls list
    :param urls:
    :return:
    """
    for url in urls:
        print("\nbegin to spider url:",url)
        try:
            result = spider_url(url)
            print("spider success,result is", result)
        except Exception as e:
            print("spider exception:",e,url)



spider_urls(urls)