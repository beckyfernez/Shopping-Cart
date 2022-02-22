
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDER_ADDRESS = os.getenv('SENDER_ADDRESS', default='SENDER_ADDRESS')
SENDGRID_TEMPLATE_ID = os.getenv('SENDGRID_TEMPLATE_ID', default='SENDGRID_TEMPLATE_ID')

message = Mail(
    from_email=SENDER_ADDRESS, 
    to_emails=SENDER_ADDRESS,)
    #subject='Sending with Twilio SendGrid is Fun',
    #html_content='<strong>and easy to do anywhere, even with Python</strong>')
message.template_id = SENDGRID_TEMPLATE_ID


try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(type(e))
    print(e)