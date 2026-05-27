#enrique
#init
import webbrowser
import time
#functions
url=["https://tinyurl.com/u57ydmaw", #punch
     "https://tinyurl.com/wjbrwcrt", #mandrill
     "https://tinyurl.com/ms8wsk9k", #harambe
     "https://tinyurl.com/mvs6y76j" #orangutan
     ]
def monkeys():
    print("Welcome to monkey reccomendation")
    time.sleep(1)
    social=input("Are you an introvert(1) or extrovert?(2): ")
    time.sleep(1)
    if social=="1":
        size=input("Do you give petite(1) or strong(2) vibes?: ")
        time.sleep(1)
        if size=="1":
            print("This is your monkey!")
            webbrowser.open(url[0])
        else:
            print("This is your monkey!")
            webbrowser.open(url[3])
    elif social=="2":
        color=input("Are you more of a colorful(1) or monochrome(2) person?: ")
        time.sleep(1)
        if color=="1":
            print("This is your monkey!")
            webbrowser.open(url[1])
        else:
            print("This is your monkey!")
            webbrowser.open(url[2])
#main
monkeys()
#sources of information

#Picture of Punch
#Website: Gizmodo
#Url: "https://gizmodo.com/punch-the-baby-monkeys-ikea-plushie-is-selling-for-hundreds-on-ebay-2000725633"
#Author: Matt Novak
#Date: February 23, 2026
#Article Title: Punch the Baby Monkey's Ikea Plushie is Selling for Hundreds on eBay
#Image Information: Baby monkey named 'Punch' is seen with a stuffed animal at a zoo on February 20, 2026,
# in north of Tokyo, Chiba Prefecture, Japan. © Photo by David Mareuil/Anadolu via Getty Images

#Picture of Mandrill
#Website: Houston Zoo
#Url: "https://www.houstonzoo.org/blog/year-of-the-monkey-mandrills/"
#Author: Dena Honeycutt
#Date: April 13, 2016
#Article Title: Year of the Monkey - Madrills

#Picture of Harambe
#Website: BBC
#URL: "https://www.bbc.com/news/newsbeat-57279486"
#Date: May 28, 2021
#Article Title: Harambe: Gorilla photo to be sold as an NFT five years after he was shot dead

#Picture of orangutan
#Website: Monkey World Ape Rescue Center
#URL: "https://monkeyworld.org/our-primates/"

