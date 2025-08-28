import os, requests, csv, time
from bs4 import BeautifulSoup

def wiki_get(url):

    save_dir = './wiki'
    html = requests.get(url).text
    print('2秒待機中')
    time.sleep(2)
    return html

target_url = 'https://ja.wikipedia.org/wiki/%E3%83%91%E3%83%AC%E3%82%B9%E3%83%81%E3%83%8A%E5%9B%BD'
#target_url = 'https://geohack.toolforge.org/geohack.php?language=ja&pagename=%E3%83%93%E3%82%B5%E3%82%A6&params=11_51_0_N_15_35_0_W_'
get_url = wiki_get(target_url)

def get_hint(usl,code):
    
    soup = BeautifulSoup(usl, 'html5lib')

    x=1
    hint = []
    national_code = code
    p_tag_list = soup.find_all('p')
    for p_tag in p_tag_list:
        if x==3:
            return hint
        nationa_title = p_tag.text.replace(national_code, '○○○')
        hint.append(nationa_title)
        x+=1
x = []
capital_box2 = []

def get_map(usl,national_code):
    soup = BeautifulSoup(usl, 'html5lib')

    p_tag_list = soup.select('.mw-file-element')
    for img in p_tag_list:
        try:
            if img['alt'] == national_code +'の位置':
                https = 'https:'
                url_img = https + img['src']
                x.append(url_img)
        except KeyError:
            print('No such key')

def get_geo(usl):
    soup = BeautifulSoup(usl, 'html5lib')

    a_tag_list = soup.select('.external')
    print(a_tag_list)
    for img in a_tag_list:
        try:
            img
            print(img)
            x.append(img.text)
            break
        except KeyError:
            print('No such key')
                         
def get_capital(url):
    soup = BeautifulSoup(url, 'html5lib')

    text_tag_list = soup.select('.infoboxCountryDataB')
    print(text_tag_list)
    get_capital = 0
    get_info =[]
    capital_box = [] 
    for text in text_tag_list:
        #print("GET!",text.text)
        get_info.append(text.text)
        capital_box = get_info[0].split('\n')
        capital_box2 = list(filter(None, capital_box))
        print(capital_box2)
    
    for captal in capital_box2:
        try:
            if captal == '首都':
                get_capital += 1
                print("GET!",captal)
                
            elif get_capital == 1:
                print("GET首都",captal)
                x.append(captal)
                break
        except KeyError:
            print('No such key')
    print(x)
    print(len(x))

def get_wikidata(url):
    soup = BeautifulSoup(url, 'html5lib')

    text_tag_list = soup.select('.infoboxCountryDataB')
    print(text_tag_list)
    return text_tag_list
                            

get = get_wikidata(get_url)
print(get)

with open('htmldeta.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(get)

"""
res = []
with open("/home/haruki/array_captal.csv") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        res.append(line)
print(res)
print(len(res))
"""