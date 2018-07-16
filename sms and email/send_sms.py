from twilio.rest import Client
import os

def send_sms(number,twilio_num):
    """
    to send sms using twilio
    :param number:
    :param twilio:
    :return none:
    """
    # Your Account SID from twilio.com/console
    account_sid = os.environ['account_sid']
    # Your Auth Token from twilio.com/console
    auth_token  = os.environ['auth_token']

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=number, #this numner has to be register on www.twilio.com
        from_=twilio_num, #generated twilio number
        body="Hello, write message body here ")

    #print(message.sid)

def main():
    phone_number=input("Enter your mobile number :").strip()
    twilio_number=input("Enter your generated twilio number :").strip()
    send_sms(phone_number,twilio_number)

if __name__ == '__main__':
    main()


