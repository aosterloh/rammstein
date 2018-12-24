from bs4 import BeautifulSoup
import requests
from twilio.rest import Client

account_sid = 'AC1304dbfe60325948xxxxxxxxxx' # Found on Twilio Console Dashboard
auth_token = 'e8043b9284969caxxxxxxxxxxxxxx' # Found on Twilio Console Dashboard

myPhone = '+49172xxxxxxx' # Phone number you used to verify your Twilio account
TwilioNumber = '+1xxxxxxxxx' # Phone number given to you by Twilio

client = Client(account_sid, auth_token)

url = 'https://www.fansale.de/fansale/tickets/hard-heavy/ozzy-osbourne/478'
response = requests.get(url)
soup = BeautifulSoup(response.content.decode('utf-8', 'ignore'), 'html.parser', )
cities = ['BERLIN']

data = soup.find_all("li", {'class':'Dropdown-ValuesEntry'})
for x in data: 
    y = x.string.strip().encode('utf-8')
    if y in cities:
        print ("Found new city "+ y) 
        client.messages.create(
  			to=myPhone,
 			from_=TwilioNumber,
  			body='I sent a text message from Python! ' + u'\U0001f680')

