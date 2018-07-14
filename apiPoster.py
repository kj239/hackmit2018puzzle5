import requests
import time
import re

class apiPoster:
    
      def __init__(self):
          self.url = 'https://gps.hackmirror.icu/u/kj239_2f0c0d'
          self.success = "Phew!"
          self.glitch = "Connection failed!"
          self.invalid = "You are stuck"
        
      def addurl(self,url):
          self.url = url
      
      def ismovevalid(self,message):
          time.sleep(0.5) #sleep 0.3 seconds after posting
          #returns 2 if success, 1 if glitch, 0 if invalid
          if message.find(self.success) > -1:
              return 2
          elif message.find(self.glitch) > -1:
              return 1
          else:
              return 0
          
      def getposition(self):
          r = requests.get('https://gps.hackmirror.icu/api/position?user=kj239_2f0c0d')
          message = str(r.text)
          [x,y] = [int(s) for s in re.findall(r'\d+',message)]
          return (x,y)
        
      def moveleft(self):
          r = requests.post('https://gps.hackmirror.icu/api/move?user=kj239_2f0c0d&move=left')
          message = str(r.text)
          return self.ismovevalid(message)
          
      def moveup(self):
          r = requests.post('https://gps.hackmirror.icu/api/move?user=kj239_2f0c0d&move=up')
          message = str(r.text)
          return self.ismovevalid(message)
              
      def moveright(self):
          r = requests.post('https://gps.hackmirror.icu/api/move?user=kj239_2f0c0d&move=right')
          message = str(r.text)
          return self.ismovevalid(message)
      
      def movedown(self):
          r = requests.post('https://gps.hackmirror.icu/api/move?user=kj239_2f0c0d&move=down')
          message = str(r.text)
          return self.ismovevalid(message)
      
      def getadjList(self):
          r = requests.get('https://gps.hackmirror.icu/api/map?user=kj239_2f0c0d')
          message = str(r.text)
          substring = message[9:-2]
          m = eval(substring.split()[0])
          return m