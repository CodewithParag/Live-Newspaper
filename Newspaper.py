import requests
import json
print("News Channel")
from win32com.client import Dispatch
url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=f4b6c5fb93624d51bb3667cbbc619d91')
response = requests.get(url)
r=response.json()
sun=Dispatch("SAPI.SpVoice")
print("Hello and welcome to our live news channel, Lets have a look at the headlines first")
sun.Speak("Hello and welcome to our live news channel, Lets have a look at the headlines first")
art = r['article']
for i in art:
       print(i['title'])
       speak(i['title'])
        
print("Thanks for listening, Have a good day")
sun.Speak("Thanks for listening,Have a good day")
