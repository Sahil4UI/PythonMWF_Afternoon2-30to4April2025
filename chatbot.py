import webbrowser
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
    else:
        print("Sorry I didn't understand")
