from bs4 import BeautifulSoup as bs4
import requests, sys, time
from requests_html import HTMLSession

class GetWishlist():
    def __init__(self,
                 DEBUG=False):
        self.DEBUG = DEBUG
        if self.DEBUG: print("GetWishlist.__init__()")
        
        
        if self.DEBUG and input("Load from file?(y/n)").lower() == "y":
            self.loadFromFile = True
        else:
            self.loadFromFile = False

        self.load()
        
        self.getItems()






    def load(self):
        # This method loads the html and creates self.soup
        if self.DEBUG: print("load()")

        if self.loadFromFile:
            inputFile = input("Enter filename or empty for default (output1.html):")
            if inputFile == "":
                inputFile = 'output1.html'

            if self.DEBUG: print("Opening",inputFile)
            
            with open(inputFile, 'rb') as f:
                self.soup = bs4(f.read(), 'lxml')

        else:
            url = input("Paste wishlist url or empty for default\n")
            if url == "":
                url = 'https://www.amazon.co.uk/hz/wishlist/ls/TI11QZ0K8UER'

            session = HTMLSession()

            page = session.get(url)

            page.html.render()  # this call executes the js in the page

            if self.DEBUG and input("Save to file?(y/n").lower() == "y":
                outputFile = input("Enter filename:")
                
                if outputFile.endswith('.html') == False:
                    outputFile += ".html"

                if self.DEBUG: print("Saving",outputFile)
                    
                with open(outputFile, 'wb+') as f:
                    f.write(page.content)

            self.soup = bs4(page.text, 'html.parser')

        if self.DEBUG: print("Soup created")


    def getItems(self):
        # This method finds items in the soup and creates self.recordedData
        if self.DEBUG: print("getItems()")

        'classList is the area the table of items is located'
        classList = self.soup.find_all('ul', class_ = "a-unordered-list a-nostyle a-vertical a-spacing-none g-items-section ui-sortable")

        'itemList is the table of items in the wishlist'
        itemList = classList[0].find_all('li')

        '''
The following are spacers in the wishlist, or empty items
They need to be removed first
li[0] = spacing
li[-1] = spacing
li[-2] = spacing
'''

        del itemList[0]
        del itemList[-1]
        del itemList[-1]

        items_in_list = len(itemList)

        if self.DEBUG: print("items_in_list =",items_in_list)

        self.recordedData = []


        for item in itemList:

            itemID = item['data-itemid']
            price = float(item['data-price'])
            
            name = item.find('a', class_="a-link-normal")['title']
            href = item.find('a', class_="a-link-normal")['href']
            reviewCount = item.find('a', class_="a-size-base a-link-normal").text.split()[0]

            
                
            self.recordedData.append([itemID,href,name,price,reviewCount])

            if self.DEBUG:
                print('''
itemID = {}

href = {}

name = {}

price = {}

reviewCount = {}
'''.format(itemID,
           href,
           name,
           price,
           reviewCount))

        print("End of items")


    def getList(self):
        if self.DEBUG: print("getList()")
        return self.recordedData


if __name__ == "__main__":
    DEBUG = True
    
    bot = GetWishlist(DEBUG)




        
    
