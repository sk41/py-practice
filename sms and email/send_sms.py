from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACafd5be955dcd2ae8fbeae077fa2fe854"
# Your Auth Token from twilio.com/console
auth_token  = "aa5ae4b8c675f912a022834620583815"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+17372031940", #this numner has to be register on www.twilio.com
    from_="+18054207492", #generated twilio number
    body="Hello I am Snehal!!! how are u")

print(message.sid)