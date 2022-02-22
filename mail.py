#How to use SendGrid (Practice Template)
#https://www.youtube.com/watch?v=j-cL2xzD6s0

# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDER_ADDRESS = os.getenv('SENDER_ADDRESS', default='SENDER_ADDRESS')
SENDGRID_TEMPLATE_ID = os.getenv('SENDGRID_TEMPLATE_ID', default='SENDGRID_TEMPLATE_ID')

template_data = {
    "total_price_usd": "$27.98",
    "human_friendly_timestamp": "June 1st, 2019 10:00 AM",
    "products":[
        {"id": 100, "name": "Product 100", "price": "$9.99"},
        {"id": 200, "name": "Product 200", "price": "$3.50"},
        {"id": 300, "name": "Product 300", "price": "$1.00"},
        {"id": 200, "name": "Product 200", "price": "$3.50"},
        {"id": 100, "name": "Product 100", "price": "$9.99"}
    ]
} # or construct this dictionary dynamically based on the results of some other process :-D

message = Mail(
    from_email=SENDER_ADDRESS, 
    to_emails=SENDER_ADDRESS,)
message.template_id = SENDGRID_TEMPLATE_ID
message.dynamic_template_data = template_data


try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(type(e))
    print(e)