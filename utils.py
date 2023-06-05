import os
import re
import socket

import requests
from lxml import etree
socket.setdefaulttimeout(3)

def collect_pic(num, keyword):
    pic_url= []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    for i in range((num // 5) + 1):
        page_url = 'https://cn.bing.com/images/async?q={}&first={}&count=3&relo=4&relp=5&cw=1117&ch=689&scenario=ImageBasicHover&datsrc=N_I&layout=ColumnBased&mmasync=1&dgState=c*6_y*1582s1599s1589s1660s1720s1704_i*40_w*172&IG=B3C2B933EAED48A4A82330EC1E7A638B&SFX=2&iid=images.5659'.format(keyword, i*35)
        print("...wait-1  (●'◡'●)...")
        html = requests.get(page_url, headers=headers).text
        html = etree.HTML(html)
        conda_list = html.xpath('//a[@class="iusc"]/@m')
        for j in conda_list:
            img_url = re.search('"murl":"(.*?)"', j).group(1)
            pic_url.append(img_url)
    return pic_url

def gen_img(num, keyword,out_file):
    pic_url  = collect_pic(num, keyword)
    path = out_file
    for index,i in enumerate(pic_url):
        try:
            filename = path + '/' + str(index) + '.jpg'
            print("...wait-2  φ(゜▽゜*)♪...")
            with open(filename, 'wb+') as f:
                f.write(requests.get(i).content)
        except:
            continue

def simplyfy_word(word):
    words = word.split(",")
    return  words[0]

def gen_pic(keyword, num=5):
    keyword = simplyfy_word(keyword)
    cur_path = os.path.abspath(os.curdir)
    out_file = os.path.join(cur_path, keyword)
    if os.path.exists(out_file):
        pass
    else:
        os.makedirs(out_file)
    gen_img(num, keyword, out_file)
    open_folder(out_file)


def open_folder(path):
    os.startfile(path)









