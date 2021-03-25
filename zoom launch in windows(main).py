import time
from datetime import datetime
from pynput.keyboard import Key, Controller
#from data import lst
import webbrowser

keyboard = Controller()

isStarted = False
lst = [["https://us04web.zoom.us/j/4631716808?pwd=VzB5ZWcxSWRiUFhKWm5UU0dueXprdz09", "11:30", "11:45"]]

for i in lst:
    while True:
        if isStarted==False:
            if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]):
                webbrowser.open(i[0])
                isStarted = True
        elif isStarted == True:
            if datetime.now().hour == int(i[2].split(':')[0]) and datetime.now().minute == int(i[2].split(':')[1]):
                keyboard.press('w')
                time.sleep(1)
                keyboard.press(Key.enter)
                isStarted = False
                break
