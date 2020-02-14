from twilio.rest import Client  #import Twilio client

# Define Twilio Account SID and Auth Token
client = Client("SID", "Auth_Token")

client.messages.create(to="+11231231234",
                       from_="+11231231234",
                       body="Hello from Python!")
