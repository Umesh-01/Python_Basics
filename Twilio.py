# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

account_sid = 'enter-your-sid'
auth_token = 'enter-your-token'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        twiml='<Response><Play loop="10">https://demo.twilio.com/docs/classic.mp3</Play></Response>',
                        to='',
                        from_=''
                    )

print(call.sid)
