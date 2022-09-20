#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def main() :
    listOfSoldItems = []
    infile=open("itemsInfo2.txt","r") # open the itemsInfo2 file in read mood to load it’s data into the dictionary
    dictionary = {}
    for line in infile :   # Red line per line from the list 
        x=line.split(",")  #Then split each line by the separator "," and put the contents of the line in list to be easy to deal with them
        a=int(x[0])        # x[0]the key for the dictionary
        dictionary[a]=[x[1],float(x[2]),int(x[3]),int(x[4])]
    flag = True
    while flag:
        print("Supermarket Management System")
        print("="*30)
        print(" 1. Print items info","\n","2. Search for an item","\n","3. Add new item","\n","4. Remove an item","\n","5. Sell an item","\n","6. Update an item","\n","7. Exit")
        print("="*30)
        option=int(input("Enter your choice : "))
        if option == 1 :       # For each option we will call it’s function
            option1(dictionary)
        if option == 2 :
            option2(dictionary)
        if option == 3 :
            option3(dictionary)
        if option == 4 :
            option4(dictionary)
        if option == 5 :
            option5(dictionary,listOfSoldItems)
        if option == 6 :
            option6(dictionary)
        if option == 7 :       # If option ==7 we want to stop the loop by making flag = False
            flag = False
    infile1 = open("itemsInfo2.txt","w") # open the itemsInfo2 file in write mood to save the changes into it
    for keys in dictionary :     ## For each key in the dictionary 
        alist = dictionary[keys] # we extract the list of values of the key to load it in the file
        infile1.write(str(keys))
        infile1.write(",")
        infile1.write(alist[0])
        infile1.write(",")
        infile1.write(str(alist[1]))
        infile1.write(",")
        infile1.write(str(alist[2]))
        infile1.write(",")
        infile1.write(str(alist[3]))
        infile1.write("\n")
    infile1.close()
    
    if len(listOfSoldItems) != 0 :        # To be sure that is the list listOfSoldItems have a value 
        infile2 = open("soldItems2.txt","w") # open the soldItems2 file in write mood to save the data from the list into it
        length = int(len(listOfSoldItems)/2) #The number of the pairs in the list listOfSoldItems
        for i in range(0,length+1,2) : # The number of rows in the file
            for j in range(i,i+2) :    # The number of columns
                infile2.write(listOfSoldItems[j])
                infile2.write(",")
            infile2.write("\n")
        infile2.close() 


def option1(dictionary):
    print("SN", "   " ,"Item Name","     ","Price","   ","Available Items","   ","Sold Items")
    for keys in dictionary :     ## For each key in the dictionary 
        alist = dictionary[keys] # we extract the list of values of the key then print the contents of it in formated shape
        print(keys,"%10s"%alist[0],"%11s"%alist[1],"%11s"%alist[2],"%18s"%alist[3])
def option2(dictionary):                                     
        print("-"*10,"Search an item","-"*10)
        print(" 1. By Serial Number.","\n","2. By Item Name.")
        choice = int(input("Enter your option : "))
        if choice==1:
            serialNumber=input("Enter serial number of the item : ")
            while not serialNumber.isdigit() :  # the serial number should be in digit if not the user shold enter it another time untile its in digit
                print("The serial number should be in digits!!")
                serialNumber = input("Enter serial number of the item again : ")
            if serialNumber.isdigit() :
                while len(serialNumber) != 4: # the serial number should be 4 digits if not the user shold enter it another time untile its 4 digits
                    print("serialNumber should be 4 digit .")
                    serialNumber=input("Enter serial number of the item again : ")
                if len(serialNumber) == 4:
                    serialNumber1=int(serialNumber)
                    while serialNumber1 not in dictionary:# the serial number should be in dictionary if not the user shold enter it another time untile its in dictionary
                        print("Found no matching item")
                        serialNumber=input("Enter serial number of the item again : ")
                    if serialNumber1 in dictionary:
                        print("Found a matching item .")
                        alist = dictionary[serialNumber1] # we extract the list of values of the key then print the contents of it in formated shape
                        print("SN", "   " ,"Item Name","     ","Price","   ","Available Items","   ","Sold Items")
                        print(serialNumber1,"%10s"%alist[0],"%11s"%alist[1],"%11s"%alist[2],"%18s"%alist[3]) 
    
        else:
            Nameofitem=input("Enter item name or part of it : " )
            count = 0
            for keys in dictionary :# For each key we extract the list of values of the key
                alist = dictionary[keys]
                if Nameofitem in alist[0] or Nameofitem == alist[0]: # we compare the name of item in the list with the entered name
                    count = 1                                        ## if the result of the comparison is true then set count = 1 and print the information of this item
          
            if count == 1:
                    print("SN", "   " ,"Item Name","     ","Price","   ","Available Items","   ","Sold Items")
                    for keys in dictionary :
                        alist = dictionary[keys]
                        if Nameofitem  in alist[0] or Nameofitem == alist[0]:
                            print(keys,"%10s"%alist[0],"%11s"%alist[1],"%11s"%alist[2],"%18s"%alist[3])
            else:       
                print("Item Name not found .")     
            
def option3(dictionary) :
        print("-"*10,"Add a new item","-"*10)
        serialNumber = input("Enter the serial number: ")
        
        if not serialNumber.isdigit() :  # the serial number should be in digit if not the user shold enter it another time untile its in digit
            flag = True
            while flag :
                print("The serial number should be in digits")
                serialNumber = input("Please enter the serial number again: ")
                if serialNumber.isdigit() :
                    flag = False
                
        if len(serialNumber) != 4: # the serial number should be 4 digits if not the user shold enter it another time untile its 4 digits
            flag = True
            while flag :
                print("The length of serial number should be equal to 4")
                serialNumber = input("Please enter the serial number again: ")
                if len(serialNumber) == 4 :
                    flag = False
        if int(serialNumber) in dictionary : 
            flag = True
            while flag :
                print("Serial numer already exists !")
                serialNumber = input("Please enter the serial number again: ")
                if int(serialNumber) not in dictionary :# the serial number should be not in dictionary if not the user shold enter it another time untile its not in dictionary
                    flag = False
                    
        itemName = input("Enter the name of the item: ")
        while  not itemName.isalpha() : #The name of the item should be in letter, if not the user shold enter it another time untile its in letters
            print("The name of the item should be in letters !!")
            itemName = input("Please enter the item name again: ")
            
        price = input("Enter the price of the item: ")
        while len(price) == 0 or price.isspace() : #if the user enter blank or doesn’t enter any thing the user shold enter it another time untile its right
            print("The price should be in digits")
            price = input("Please enter the price of the item again: ")
        while price.isalpha() : # the price should be in digit if not the user shold enter it another time untile its in digit
            print("The price should be float positive number")
            price = input("Please enter the price of the item again: ")
        while float(price) < 0.0 :# the price should be greater than 0 if not the user shold enter it another time untile its right
            print("The the price of the item should be float positive number: ")
            price = input("Please enter the price of the item again: ")
        
        numberOfAvailableItems = input("Enter the number of available items in the supermarket: ")
        while not numberOfAvailableItems.isdigit() :
            print("The numberOfAvailableItems should be integer positive number")
            numberOfAvailableItems = input("Please enter the number of available items in the supermarket again: ")  
        while int(numberOfAvailableItems) < 0 :
            print("The the number of available items in the supermarket should be integer positive number: ")
            numberOfAvailableItems = input("Please enter the number of available items in the supermarket again: ")
        soldItems = 0
        print("Item has been added successfully !!!")   
        dictionary[int(serialNumber)] = [itemName,float(price),int(numberOfAvailableItems),soldItems] #add the new item to the dictionary
       
def option4(dictionary):
    print("-"*10,"Remove an item","-"*10)
    serialNumber = int(input("Enter the serial number: "))
     
    while serialNumber not in dictionary: # the serial number should be not in dictionary if not the user shold enter it another time untile its not in dictionary
        print("Serial number not found !!")
        serialNumber = int(input("Enter the serial number again : ")) 
        if serialNumber not in dictionary:
            print("Serial number not found !!")
            serialNumber = int(input("Enter the serial number again : "))
        
        
    if serialNumber  in dictionary:
        alist = dictionary[serialNumber]
        print("SN", "   " ,"Item Name","     ","Price","   ","Available Items","   ","Sold Items")
        print(serialNumber,"%10s"%alist[0],"%11s"%alist[1],"%11s"%alist[2],"%18s"%alist[3])
        if alist[3] == 0: #If the number of sold items not equal to zero the program don’t delete the item 
            print("-"*10,"Are you sure you want to delete the item ? ","-"*10)
            print("%27s" % " 1- Yes ", " or ", " 2- No ")
            choice=int(input("Enter your choice 1 or 2 : "))
            if choice == 1:
                delet=dictionary.pop(serialNumber) # delete the key so all the item should be deleted
                print("The item has been deleted successfully :)")
                
            elif choice == 2: # Don’t delete any thing
                print("The item has not been deleted.")
        else:
            print("The deletion failed because of the item has some sold copies.") 
def option6(dictionary) :
        print("-"*10,"Update an item","-"*10)
        serialNumber = input("Enter the serial number of the item: ")
        
        if not serialNumber.isdigit() :# the serial number should be in digit if not the user shold enter it another time untile its in digit
            flag = True
            while flag :
                print("The serial number should be in digits")
                serialNumber = input("Please enter the serial number again: ")
                if serialNumber.isdigit() :
                    flag = False
                
        if len(serialNumber) != 4: # the serial number should be 4 digits if not the user shold enter it another time untile its 4 digits
            flag = True
            while flag :
                print("The length of serial number should be equal to 4")
                serialNumber = input("Please enter the serial number again: ")
                if len(serialNumber) == 4 :
                    flag = False
        if int(serialNumber) not in dictionary : # the serial number should be in dictionary if not the user shold enter it another time untile its in dictionary
            flag = True
            while flag :
                print("Serial numer does not exist !")
                serialNumber = input("Please enter the serial number again: ")
                if int(serialNumber) in dictionary :
                    flag = False
                    
        print(" 1.Name\n","2.Available Items")
        
        choice = input("What would you like to update ? ") # the user should choose between updata the name by enter "1" or update the number of available items by enter "2"
        if choice == "1" :                        
            name = input("Enter the new name of the item: ")
            while  not name.isalpha() : #The name of item should be in letters, if not the user should enter it again until it correct
                print("The name of the item should be in letters !!")
                name = input("Please enter the item name again: ")
            alist = dictionary[int(serialNumber)] # we extract the list of values of the key
            alist[0] = name                       ## then update the name in the dictionary with the new name
            dictionary[int(serialNumber)] = [alist[0],alist[1],alist[2],alist[3]]
            
        elif choice == "2" :
            availableItems = input("Enter the new available number of items: ")
            while not availableItems.isdigit() :# the number of available items should be in digit if not the user shold enter it another time untile its in digit
                print("The number of available items should be in digits !!")
                availableItems = input("Enter the new available number of items again: ")
            alist = dictionary[int(serialNumber)] # we extract the list of values of the key
            alist[2] = int(availableItems)        ## then update the number of available items in the dictionary with the new number of available items
            dictionary[int(serialNumber)] = [alist[0],alist[1],alist[2],alist[3]]
        print("It has been updated successfully :)")

def option5(dictionary,listOfSoldItems) :
        print("-"*10,"Sell an item","-"*10)
        serialNumber = input("Enter the serial number of the item: ")
        
        if not serialNumber.isdigit() : # the serial number should be in digit if not the user shold enter it another time untile its in digit
            flag = True
            while flag :
                print("The serial number should be in digits")
                serialNumber = input("Please enter the serial number again: ")
                if serialNumber.isdigit() :
                    flag = False
                
        if len(serialNumber) != 4: # the serial number should be 4 digits if not the user shold enter it another time untile its 4 digits
            flag = True
            while flag :
                print("The length of serial number should be equal to 4")
                serialNumber = input("Please enter the serial number again: ")
                if len(serialNumber) == 4 :
                    flag = False
        if int(serialNumber) not in dictionary : # the serial number should be in dictionary if not the user shold enter it another time untile its in dictionary
            flag = True
            while flag :
                print("Serial numer does not exist !")
                serialNumber = input("Please enter the serial number again: ")
                if int(serialNumber) in dictionary :
                    flag = False
        name = input("Enter the name of the person who bought this item: ") # Enter the name of the person who bought this item and it should be in letter
        while  not name.isalpha() :                                         ## If not the user should enter it again until it correct
                print("The name should be in letters !!")
                name = input("Please enter the name of the person who bought this item again: ")
        print("Item has been sold to %s successfully :)"%name)
        listOfSoldItems.append(serialNumber)  # Add the serial number to the list listOfSoldItems
        listOfSoldItems.append(name)          # Add the name to the list listOfSoldItems
        alist = dictionary[int(serialNumber)] # # we extract the list of values of the key
        dictionary[int(serialNumber)] = [alist[0],alist[1],(alist[2]-1),(alist[3]+1)] # Then the number of available item should be reduced and the number of sold items should be incremented in the dictionary
        
main()


# In[ ]:




