from twilio.rest import Client
import os

# Your Account SID from twilio.com/console
account_sid = os.environ['account_sid']
# Your Auth Token from twilio.com/console
auth_token  = os.environ['auth_token']

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+17372031940", #this numner has to be register on www.twilio.com
    from_="+18054207492", #generated twilio number
    body="Hello I am Snehal!!! how are u")

print(message.sid)