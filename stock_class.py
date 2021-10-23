# -*- coding: utf-8 -*-
"""
Created By: D40907517
Created On: 10/10/2021
@author Johnathan Alexander
"""

class Stock:
    def __init__(self, newSymbol, newName, newShares ):
        self.symbol=newSymbol
        self.name=newName
        self.shares=newShares
        self.DataList=[]
    
    def add_data(self, stock_data):
        self.DataList.append(stock_data)
    
    def print_item(self):
        print("Stock:\nSymbol: "+self.symbol+"\tName: "+self.name + "\tShares: "+ str(self.shares))
        for d in self.DataList:
            d.print_item()
class DailyData :
    def __init__(self, newDate, newClose, newVolume):
        self.date=newDate
        self.close=newClose
        self.volume=newVolume
    
    def print_item(self):
        print("\tDaily Data:\n\tDate: "+self.date+"\tClose: "+str(self.close)+"\tVolume: "+str(self.volume))

# Unit Test - Do Not Change Code Below This Line *** *** *** *** *** *** *** *** ***
# main() is used for unit testing only. It will run when stock_class.py is run.
# Run this to test your class code. Once you have eliminated all errors, you are
# ready to continue with the next part of the project.

def main():    
    error_count = 0    
    error_list = []    
    print("Unit Testing Starting---")   
    # Test Add Stock    
    print("Testing Add Stock...",end="")    
    try:
        testStock = Stock("TEST","Test Company",100)        
        print("Successful!")    
    except:        
        print("***Adding Stock Failed!")
        error_count = error_count+1
        error_list.append("Stock Constructor Error")    
    # Test Change Symbol    
    print("Test Change Symbol...",end="")    
    try:
        testStock.symbol = "NEWTEST"
        if testStock.symbol == "NEWTEST":
            print("Successful!")
        else: 
            print("***ERROR! Symbol change unsuccessful.")
            error_count = error_count+1            
            error_list.append("Symbol Change Error")    
    except:        
        print("***ERROR! Symbol change failed.")        
        error_count = error_count+1        
        error_list.append("Symbol Change Failure")    
    print("Test Change Name...",end="")    
    try:        
        testStock.name = "New Test Company"        
        if testStock.name == "New Test Company":            
            print("Successful!")        
        else:            
            print("***ERROR! Name change unsuccessful.")            
            error_count = error_count+1            
            error_list.append("Name Change Error")    
    except:        
        print("***ERROR! Name change failed.")        
        error_count = error_count+1        
        error_list.append("Name Change Failure")        
        print("Test Change Name...",end="")    
    try:        
        testStock.shares = 2000        
        if testStock.shares == 2000:            
            print("Successful!")        
        else:            
            print("***ERROR! Shares change unsuccessful.")            
            error_count = error_count+1            
            error_list.append("Shares Change Error")   
    except:        
        print("***ERROR! Shares change failed.")        
        error_count = error_count+1        
        error_list.append("Shares Change Failure")    
         
    # Test add daily data    
    print("Creating daily stock data...",end="")    
    daily_data_error = False    
    try:        
        dayData = DailyData("1/1/20",float(14.50),float(100000))        
        testStock.add_data(dayData) 
        if testStock.DataList[0].date != "1/1/20":            
            error_count = error_count + 1            
            daily_data_error = True            
            error_list.append("Add Daily Data - Problem with Date")
        if testStock.DataList[0].close != 14.50:            
            error_count = error_count + 1           
            daily_data_error = True            
            error_list.append("Add Daily Data - Problem with Closing Price")
        if testStock.DataList[0].volume != 100000:            
            error_count = error_count + 1            
            daily_data_error = True            
            error_list.append("Add Daily Data - Problem with Volume")      
    except:        
        print("***ERROR! Add daily data failed.")        
        error_count = error_count + 1        
        error_list.append("Add daily data Failure!")        
        daily_data_error = True    
    if daily_data_error == True:        
        print("***ERROR! Creating daily data failed.")    
    else:        
        print("Successful!")    
        
    if (error_count) == 0:        
        print("Congratulations - All Tests Passed")    
    else:        
        print("-=== Problem List - Please Fix ===-")        
        for em in error_list:            
            print(em)    
        print("Goodbye")
            
# Program Starts Here
if __name__ == "__main__":    
    # run unit testing only if run as a stand-alone script  
    print("Running tests!!!") 
    main()
    # testStock = Stock("TEST","Test Company",100)
    # testStock.add_data(DailyData("10/12/2021",float(14.50),float(100000)))
    # testStock.add_data(DailyData("1/1/20",float(14.50),float(100000)))
    # testStock.print_item()
    # print("Finished!!")