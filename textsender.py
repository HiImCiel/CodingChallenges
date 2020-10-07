# Sends a text using Twilio
from twilio.rest import Client
import os

# Google API & Twilio keys are saved in a txt file
print("Enter absolute file path of your credentials txt file:")
credentialsfilepath = input()

# Splits txt file up to retreive only the keys
if os.path.exists(credentialsfilepath):
    readfile = open(credentialsfilepath)
    contents = readfile.read()
    splitcontents = contents.split()

    keyarray = splitcontents[2::3]
    google_apikey = keyarray[0]
    account_sid = keyarray[1]
    auth_token = keyarray[2]

# Creates a client object based on credentials
    client = Client(account_sid, auth_token)

    # print(google_apikey)
    # print(account_sid)
    # print(auth_token)
    # print(splitcontents)
    # print(keyarray)
else:
    ValueError("That file does not exist")


# Sends a text to a number with the message content as the argument
def sendmessage(message):
    client.messages.create(body=message, from_='+13342588359', to='+19803093642')


sendmessage("Hello there General Kenobi")
