from twilio.rest import Client  #import Twilio client

# Define Twilio Account SID and Auth Token
client = Client("AC830313aa4bd1f45c0489b5921215a792", "a7485e7fc5659a28b365219aa6959036")

client.messages.create(to="+11231231234",
                       from_="+11231231234",
                       body="Hello from Python!")
