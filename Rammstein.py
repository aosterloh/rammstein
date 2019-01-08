# coding=utf-8
from bs4 import BeautifulSoup
import requests
from twilio.rest import Client
import time
import random
import datetime


#Twilio Setup
account_sid = 'AC1304dbfe6032xxxxxxxxxx' # Found on Twilio Console Dashboard
auth_token = 'e8043b9284969caxxxxxxxxxx' # Found on Twilio Console Dashboard
myPhone = '+49172xxxxxxxx' # Phone number you used to verify your Twilio account
TwilioNumber = '+1xxxxxxxxxx' # Phone number given to you by Twilio
cities = ['berlin', 'bern', 'münchen', 'hamburg', 'frankfurt', 'dresden', 'rostock', 'gelsenkirchen', 'barcelona', 'copenhagen', 'k$

client = Client(account_sid, auth_token)
client.messages.create(to=myPhone, from_=TwilioNumber,
                body='Programm Start')

while True:
        #testurl = 'https://www.fansale.de/fansale/tickets/hard-heavy/ozzy-osbourne/478'
        url = 'https://www.fansale.de/fansale/tickets/alle/rammstein/526'

        response = requests.get(url)
        soup = BeautifulSoup(response.content.decode('utf-8', 'ignore'), 'html.parser', )
        data = soup.find_all("li", {'class':'Dropdown-ValuesEntry'})
        for x in data: 
            y = x.string.strip().lower().encode('utf-8')
            print
            if y in cities:
                client.messages.create(to=myPhone, from_=TwilioNumber,
                body='Good News: Rammstein Tix available at http://bit.ly/2EOTQQ0')
        sleeptime = 300+random.randint(100,200)    
        #print 'sleeping ' + str(sleeptime) + ' seconds' 
        now = datetime.datetime.now()
        if (now.hour==9) and (now.minute<15):
                client.messages.create(to=myPhone, from_=TwilioNumber,
                 body='Daily Rammstein Hello')  
        time.sleep(sleeptime)
