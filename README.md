
# Shopping-Cart

A Completed Repository for the ["Shopping Cart" Project](https://github.com/prof-rossetti/intro-to-python/blob/main/projects/shopping-cart/README.md).

Some descriptions have been adapted from the Tic-Tac-Toe repository, "Command-line Computing" Exercise, and Shopping Cart Project belonging to Professor Rossetti.

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip
  + SendGrid

## Setup

Optionally fork this [remote repository](https://github.com/beckyfernez/Shopping-Cart), to create a copy under your own control. Then "clone" or download the remote repository (or your forked copy) onto your local computer, for example to your Desktop. Then navigate to wherever you downloaded the repo:

```sh
cd ~/Desktop/Shopping-Cart
```

Create a virtual environment:

```sh
conda create -n shopping-env python=3.8
```

Activate the virtual environment:

```sh
conda activate shopping-env
```

Install package dependencies (mainly for testing):

```sh
pip install -r requirements.txt
```

## Environment Variables

In order to run the two implemented bonus objectives (varying tax rates and email receipts), you need to create your own environment variables in a .env file.

Create .env file:

```sh
touch .env
```

Edit and save a file, using a command-line utility provided by your preferred text editor (like VS Code):

```sh
code .env
```

Create environmental variables within .env file (Example Code):

```sh
# this is the ".env" file... with environment variables

TAX_RATE=0.06

SENDER_ADDRESS='from_email@example.com'

SENDGRID_TEMPLATE_ID='YOUR_SENDGRID_TEMPLATE_ID'
```

NOTE: The ".env" file must be ignored from version control, by using a corresponding entry in the ".gitignore" file.

```sh
# this is the ".gitignore" file...

# ignore environment variables in the ".env" file:
.env
```

Link your Sendgrid API Key:

On your SendGrid page, create a new API Key and integrate using a Web API. You will then be prompted to run the following in your terminal/shell:

```sh
echo "export SENDGRID_API_KEY='YOUR_SENDGRID_API_KEY'" > sendgrid.env
echo "sendgrid.env" >> .gitignore
source ./sendgrid.env
```

Install the package:
```sh
pip install sendgrid
```

You are now ready to run the two bonus objectives.

## Usage

Configure your own tax rate according to your sales region and run the shopping cart program:

Install python-dotenv to read key-value pairs from a .env file:

```sh
pip install python-dotenv
```

Enter tax rate percent as a decimal:
```sh
TAX_RATE=0.0875 python shopping_cart.py
```

OR

Continue with default tax rate, 0.06 (D.C. sales tax rate), and run the shopping cart program:

```sh
python shopping_cart.py
```

You will be asked if you would wish to receive your receipt by email. If 'YES' is selected, you will be prompted to enter a customer email. If 'NO' is selected, the program will complete and exit. 

NOTE: If you have not configured the environment variables for the receipt email, enter 'NO' when asked if you would wish to receive your receipt by email.

## Demo

Here is a demonstration of the application:

```
Please input a product identifier, or 'DONE' if there are no more items: 2
Please input a product identifier, or 'DONE' if there are no more items: 3
Please input a product identifier, or 'DONE' if there are no more items: 4
Please input a product identifier, or 'DONE' if there are no more items: DONE
-------------------------------
COBRA GROCERY
-------------------------------
Address:
3700 O St. NW
Washington, DC 20057

Website: www.cg.com
Phone: 202.687.5874
Checkout Time: 2022-02-18 07:42 PM
-------------------------------
Shopping Cart Items:
+ All-Seasons Salt ($4.99)
+ Robust Golden Unsweetened Oolong Tea ($2.49)
+ Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce ($6.99)
-------------------------------
Subtotal:  $14.47
Sales Tax (6.00%):  $0.87
Total:  $15.34
-------------------------------
Would you wish to receive your receipt by email? 'YES' or 'NO': YES
Enter customer email: to_email@example.com
202
b''
Server: nginx
Date: Tue, 22 Feb 2022 10:18:57 GMT
Content-Length: 0
Connection: close
X-Message-Id: fFikgMfYQ--Ys55w_gOQ0A
Access-Control-Allow-Origin: https://sendgrid.api-docs.io
Access-Control-Allow-Methods: POST
Access-Control-Allow-Headers: Authorization, Content-Type, On-behalf-of, x-sg-elas-acl
Access-Control-Max-Age: 600
X-No-CORS-Reason: https://sendgrid.com/docs/Classroom/Basics/API/cors.html
Strict-Transport-Security: max-age=600; includeSubDomains
-------------------------------
Your receipt has been sent. Thanks for your business, and please come again!
-------------------------------
```
