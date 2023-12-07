import csv
from GetWishlist import GetWishlist
from datetime import datetime

class Main():
    def __init__(self,DEBUG):
        self.DEBUG = DEBUG
        if self.DEBUG: print("Main.__init__()")

        wishlistBot = GetWishlist(DEBUG)
        self.onlineList = wishlistBot.getList()

        self.save()




    def save(self):
        if self.DEBUG: print("save()")

        storedCSV = input("Enter filename to store this data or empty for default:")
        if storedCSV == "": storedCSV = "saved.csv"
        if storedCSV.endswith('.csv') == False:
            storedCSV += ".csv"
        
        try:
            with open(storedCSV,'r') as f:
                # do existing stuff
                if DEBUG: print("Reading",storedCSV)
            
        except FileNotFoundError:
            if DEBUG: print("Creating",storedCSV)
            
            with open(storedCSV,'w') as f:
                # do new file stuff
                writer = csv.writer(f)

                header = ['format=itemID','href','name','startRecordDate','lastRecordDate','startPrice','startReviewCount',r'priceUpdates=[[newPrice,currentDate]]',r'reviewCountUpdates=[[newReviewCount,currentDate]]']
                writer.writerow(header)
                
                dateToday = datetime.today().strftime('%d-%m-%Y')
                
                for item in self.onlineList:
                    if self.DEBUG: print("itemList=",item)
                    
                    row = item[:3] # itemID, href, name
                    row.append(dateToday) # startRecordDate
                    row.append(dateToday) # lastRecordDate
                    row.append(item[3]) # startPrice
                    row.append(item[4]) # startReviewCount
                    row.append('priceUpdates=[]')
                    row.append('reviewCountUpdates=[]')
                    
                    if self.DEBUG: print("\nAdding row:",row)
                    writer.writerow(row)
        


        





    

if __name__ == "__main__":
    DEBUG = True
    
    bot = Main(DEBUG)
