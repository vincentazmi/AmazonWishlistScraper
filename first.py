from bs4 import BeautifulSoup as bs
import requests, sys, time
from requests_html import HTMLSession

url = input("Paste wishlist url or empty for default\n")
if url == "":
    url = 'https://www.amazon.co.uk/hz/wishlist/ls/TI11QZ0K8UER?ref_=wl_share'


outputFile = 'output1.html'
loadSoup = True

if loadSoup:
    with open(outputFile, 'rb') as f:
        soup = bs(f.read(), 'lxml')
else:

    session = HTMLSession()

    page = session.get(url)

    page.html.render()  # this call executes the js in the page

    with open(outputFile, 'wb+') as f:
        f.write(page.content)


    soup = bs(page.text, 'html.parser')
        


'classList is the area the table of items is located'
classList = soup.find_all('ul', class_ = "a-unordered-list a-nostyle a-vertical a-spacing-none g-items-section ui-sortable")

'itemList is the table of items in the wishlist'
itemList = classList[0].find_all('li')

'''
li[0] = spacing
li[-1] = spacing
li[-2] = spacing
'''

del itemList[0]
del itemList[-1]
del itemList[-1]

items_in_list = len(itemList)

print(items_in_list)


for item in itemList:
    price = float(item['data-price'])
    name = item.find('a', class_="a-link-normal")['title']
    refID = item['data-itemid']
##    print('review_count_'+refID)
    tagA = item.find_all('a')#, id_='review_count_'+refID)
    
    for i,x in enumerate(tagA):
        try:
            y = x['id']
            if y == 'review_count_'+refID:
##                print(i,y,x.text)
                reviewCount = x.text.strip()
            else: raise
        except Exception as e:
            pass
##            print(i,"nah",e)
##        print(x,'\n'+'*****************'+'\n')
    print(name)
    print(price)
    print(reviewCount)    
    
    
    
    print('\n******************************************************\n')

'''
<ul id="g-items", class="a-unordered-list a-nostyle a-vertical a-spacing-none g-items-section ui-sortable>">
'''
