import requests 
from bs4 import BeautifulSoup 
import os
import time
import json

#Opening The Settings.json file
with open('c:/Users/japba/Desktop/Projects/Jarvis/settings.json','r') as file:
    settings = json.load(file)

URL = settings['url'] # the URL we are going to use
my_price = settings['budget'] # Set your budget
headers = {"User-Agent": settings['user-agent']}  # Google "My User Agent" And Replace It
currency_symbols = ['€', '£', '$', "¥", "HK$", "₹", "¥", ","] # initializing Currency Symbols to substract it from our string

#Checking the price
def checking_price():
    page = requests.get(URL, headers=headers)
    soup  = BeautifulSoup(page.content, 'html.parser')

    if "amazon" in URL:
        try: 
            #Finding the elements
            product_title = soup.find(id="productTitle").get_text().strip()
            product_price = soup.find(id="priceblock_ourprice").get_text()

            # using replace() to remove currency symbols
            for i in currency_symbols : 
                product_price = product_price.replace(i, '')

            #Converting the string to integer
            product_price = int(float(product_price))
            print("The Product Name is:" ,product_title.strip())
            print("The Price is:" ,product_price)

            # checking the price
            if(product_price<my_price):
                result ="You Can Buy This Now!"
                print("You Can Buy This Now!")
                time.sleep(3) # audio will be played first then exit the program. This time for audio playing.
            else:
                result = "The Price Is Too High!"
                print("The Price Is Too High!")
            return  "Error! Not Available"
        except:
            result = "Error! Not Available"
            return result      

    elif "flipkart" in URL:
        try:
            #Finding the elements
            product_title = soup.find(class_="B_NuCI").get_text().strip()
            product_price = soup.find(class_="_30jeq3 _16Jk6d").get_text()

            # using replace() to remove currency symbols
            for i in currency_symbols : 
                product_price = product_price.replace(i, '')

            #Converting the string to integer
            product_price = int(float(product_price))

            # checking the price
            if(product_price<my_price):
                result ="You Can Buy This Product"+str(product_title)+" Now! The Price is "+str(product_price)+", which is under your budget!"
                # print(result)
                time.sleep(3) # audio will be played first then exit the program. This time for audio playing.
            else: 
                result = "The Price of the product "+str(product_title)+" is "+str(product_price)+", Which is Too High, According to your budget !"
                # print(result)
            return result
        except:
            result = "Error! Not Available"
            return result
    else:
        return "Vendor not recognized"


def run():
    while True:
        result = checking_price()
        #time.sleep(settings['remind-time']) #It is set to run the program once in an hour! You can change by changing the value in seconds!
        print(result)
        return result
        

run()