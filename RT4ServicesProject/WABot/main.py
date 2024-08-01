""""""
import os, sys 
from twilio.rest import Client


def main():
    # Download the helper library from https://www.twilio.com/docs/python/install


    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
        from_="+15017122661",
        to="+15558675310",
    )

    sys.stdout.write(message.body)

if __name__ == '__main__':
    print("Starting the bot")
    while True:
        main()