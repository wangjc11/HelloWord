from selenium import webdriver
import requests
import json
import re
from urllib.request import urlretrieve



def get_url():
    url = "https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w={}".format(name)
    # headers = {‘User-Agent’:'mozilla/5.0 (windows nt 6.1; wow64) applewebkit/537.36 (khtml, like gecko) chrome/27.0.1453.94 safari/537.36'}
    # requests.get(url, headers = headers)
    driver.get(url)
    driver.implicitly_wait(5)   # 等待5秒，如果页面2秒加载完毕，则不用等待5秒
    data = driver.find_element_by_xpath('//*[@id="song_box"]/div[2]/ul[2]/li[4]/div/div[2]/span[1]/a').get_attribute('href')
    # element 与elements 不一样，记得区分
    print(data)
    data = {'mid': data}    # 将 data 数据改为 字典 类型，才能别下面的requests接收
    return(data)

def get_music_url(data):
    url = "http://www.douqq.com/qqmusic/qqapi.php"
    req = requests.post(url, data = data).text
    req = json.loads(req)   # json 模块，不懂
    req = req.replace('\/', '/')   # replace 替换，前一个参数为被替换的字符，后面为替换后的字符
    print(req)
    rg = re.compile('mp3_l":"(.*?),"')   # 正则。。。还不会
    rs = re.findall(rg, req)[0]    # 从req中拿到符合上一行条件的rg，并且只取第一个元素
    return rs

def get_music(rs):
    urlretrieve(rs, name + '.mp3')


def go():
    data = get_url()
    rs = get_music_url(data)
    get_music(rs)

if __name__ == '__main__':
    name = input("请输入你想要下载的歌曲：")
    driver = webdriver.Chrome()
    go()