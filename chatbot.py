import webbrowser
import os
import glob
import urllib.request as url  #sends request and return response
import bs4 #bs4 is used to fetch data
import random
# but bs4 is not preinstalled ,you have to install it by using "pip install bs4" in cmd
from datetime import datetime
chat = True
byeIntent = ["bye","bie","tata","see you","ttyl"]
helloIntent = ["hey","hi"]

while chat:
    msg = input("Enter Msg : ")
    if msg in helloIntent:
        print("Hi....")
    elif msg in byeIntent:
        print("Bye...See you later!")
        chat = False
    elif "time" in msg:
        dt=datetime.now()
        print(dt.strftime("%H:%M:%S,%p"))
        # date
    elif "date" in msg:
        dt = datetime.now()
        print(dt.strftime("%d-%m-%y,%a"))    
    elif msg.startswith("open"):
        webbrowser.open(msg.split()[-1]+".com")
    elif "play" in msg:
        musicList = glob.glob("*.mp3")
        # for i in range(len(musicList)):
        #     print(i+1 , musicList[i])
        # choice = int(input("Enter music no from above : "))
        # os.startfile(musicList[choice])
        os.startfile(random.choice(musicList))
        
        
    elif "news" in msg:
        path = "https://indianexpress.com/section/"
        choice = input("Press 1 for Politics\nPress 2 for Business\nPress 3 for Sports")
        if choice == "1":
            path += "political-pulse"
            response = url.urlopen(path)
            data = bs4.BeautifulSoup(response,features="html.parser")
            h2_list = data.findAll("h2",class_="title")
            for item in h2_list:
                print(item.text)
                print("\n***************************************\n")
    else:
        print("Sorry I didn't understand")
