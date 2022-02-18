import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

#SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
#SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")

#client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
#client = SendGridAPIClient("rebecca.mfdz@gmail.com") #> <class 'sendgrid.sendgrid.SendGridAPIClient>
#print("CLIENT:", type(client))

subject = "Your Receipt from the Green Grocery Store"

html_content = "Hello World"
#print("HTML:", html_content)

# FYI: we'll need to use our verified SENDER_ADDRESS as the `from_email` param
# ... but we can customize the `to_emails` param to send to other addresses
#message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS, subject=subject, html_content=html_content)
message = Mail(from_email="rebecca.mfdz@gmail.com", 
               to_emails="rmf83@georgetown.edu", 
               subject=subject, 
               html_content=html_content)

try:
    client = SendGridAPIClient(os.environ['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'])
    response = client.send(message)

    print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
    print(response.status_code) #> 202 indicates SUCCESS
    print(response.body)
    print(response.headers)

except Exception as err:
    print(type(err))
    print(err)