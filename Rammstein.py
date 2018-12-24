from bs4 import BeautifulSoup
import requests
from twilio.rest import Client
import time

#Twilio Setup
account_sid = 'xxxxxx' # Found on Twilio Console Dashboard
auth_token = 'xxxxxxx' # Found on Twilio Console Dashboard
myPhone = '+4917xxxxxxx' # Phone number you used to verify your Twilio account
TwilioNumber = '+1xxxxxxxxxxxx' # Phone number given to you by Twilio
cities = ['BERLIN', 'HAMBURG', 'FRANKFURT', 'DRESDEN', 'ROSTOCK', 'GELSENKIRCHEN', 'BARCELONA', 'COPENHAGEN', 'ROTTERDAM', 'PARIS']

while True:
    # testurl 'https://www.fansale.de/fansale/tickets/hard-heavy/ozzy-osbourne/478'
    url = 'https://www.fansale.de/fansale/tickets/alle/rammstein/526'
    client = Client(account_sid, auth_token)
    response = requests.get(url)
    soup = BeautifulSoup(response.content.decode('utf-8', 'ignore'), 'html.parser', )
    data = soup.find_all("li", {'class':'Dropdown-ValuesEntry'})
    for x in data: 
        y = x.string.strip().encode('utf-8')
        if y in cities:
            print ("Found new city "+ y) 
            client.messages.create(to=myPhone, from_=TwilioNumber,
               body='Good News: Rammstein Tix available at http://bit.ly/2EOTQQ0' + u'\U0001f680')
        else:
            print ("Found nothing new") 
    time.sleep(60)
