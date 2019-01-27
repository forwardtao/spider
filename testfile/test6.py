"try{feedCardJsonpCallback(").rstrip(");}catch(e){};")import requests
from bs4 import BeautifulSoup

headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
link='https://beijing.anjuke.com/sale/'
def getHouseInfo(link):
    r=requests.get(link,headers=headers)

    soup=BeautifulSoup(r.text,'lxml')
    house_list=soup.find_all('li',class_='list-item')

    for house in house_list:
        name=house.find('div',class_='house-title').a.text.strip()
        price=house.find('span',class_='price-det').text.strip()
        price_area=house.find('span',class_='unit-price').text.strip()#单位面积
        no_room=house.find('div',class_='details-item').span.text#几室几厅
        area=house.find('div',class_='details-item').contents[3].text
        floor=house.find('div',class_='details-item').contents[5].text
        year=house.find('div',class_='details-item').contents[7].text

        broker=house.find('span',class_='brokername').text
        broker=broker[1:]

        address=house.find('span',class_='comm-address').text.strip()
        address=address.replace('\xa0\xa0\n',' ')

        tag_list=house.find_all('span',class_='item-tags')
        tags=[i.text for i in tag_list]

        print(name,price,price_area,no_room,area,floor,year,broker,address,tags)
for i in range(1,11):
    link=link+'/p'+str(i)
    print('page'+str(i))
    getHouseInfo(link)