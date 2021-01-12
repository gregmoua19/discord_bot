from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "I do live!"

def run():
  app.run(host = '0.0.0.0', port = 8080)

def stay_up():
  t = Thread(target=run)
  t.start()
  
  #this class allowed the bot to be pinged 
  #continuously by a third party software 
  #so it wouldn't get shut down on Repl.it
