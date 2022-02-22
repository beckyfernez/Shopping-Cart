

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


subtotal = 0
selected_ids = []
matching_products = []

#BONUS 1 (Creating an environment variable)
#https://www.youtube.com/watch?v=YdgIWTYQ69A
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

#SALES TAX RATE: 6% in DC on all sales items (default)
#https://howtostartanllc.com/taxes/district-of-columbia-sales-tax#:~:text=Fortunately%2C%20D.C.%20has%20only%20a,Zip%20Code%20in%20the%20US.
TAX_RATE = os.getenv("TAX_RATE", default=0.06)
SENDER_ADDRESS = os.getenv('SENDER_ADDRESS', default='SENDER_ADDRESS')
SENDGRID_TEMPLATE_ID = os.getenv('SENDGRID_TEMPLATE_ID', default='SENDGRID_TEMPLATE_ID')

while True:

    #ASK FOR USER INPUT
    product_id = input ("Please input a product identifier, or 'DONE' if there are no more items: ")
    #print(product_id)
    #print(type(product_id))

    #VALIDATE USER INPUT
    #https://www.datasciencemadesimple.com/lower-upper-title-function-python/
    product_id = product_id.upper()

        #EXIT CODE WHEN FINISHED
    if str(product_id) == "DONE":
        break

        #STORE SELECTED ITEMS INTO NEW LIST
        #https://stackoverflow.com/questions/12140185/using-in-range-in-an-if-else-statment
    elif int(product_id) in range (1, 21):
        selected_ids.append(product_id)

        #print (selected_ids) (e.g. ['4', '5'])

    elif int(product_id) not in range (1, 21):
        print ("-------------------------------")
        print ("Product identifier not found. Please try again.")
        print ("-------------------------------")

        # TODO what if the input is a string typo? how can I get the program to not crash?
    #elif product_id != "DONE":
    #    print ("Product identifier not found. Please try again.")
    #    quit ()

#LOOK UP CORRESPONDING PRODUCTS IN NEW LIST
for product_id in selected_ids:
    for id in products:
        if str(id["id"]) == str(product_id):
        #this is a match using string conversion since the list uses integers
            matching_products.append(id)
            #print(matching_products)
    #matched_product = matching_products[0] #(0 = the placement of the item in the list?)
    #subtotal = subtotal + matched_product["price"] #this is an int
    #print (matched_product["name"], " (", to_usd(matched_product["price"]), ")")
    #print (subtotal)


#RECEIPT FORMATTING
print ("-------------------------------")
print ("COBRA GROCERY")
print ("-------------------------------")
print ("Address:")
print ("3700 O St. NW")
print ("Washington, DC 20057")
print (" ")
print ("Website: www.cg.com")
print ("Phone: 202.687.5874")


#CURRENT DATE AND TIME
#https://www.pythonprogramming.in/get-current-time-in-mst-est-utc-and-gmt.html
#https://www.programiz.com/python-programming/datetime/current-datetime
#https://stackoverflow.com/questions/1759455/how-can-i-account-for-period-am-pm-using-strftime
from datetime import datetime
from pytz import timezone
est = timezone('EST')
now = datetime.now(est)
date_time = now.strftime("%Y-%m-%d %I:%M %p")
print ("Checkout Time:", date_time)
print ("-------------------------------")
print ("Shopping Cart Items:")


#RETURN SELECTED PRODUCTS
for products in matching_products:
    name = str(products["name"])
    price = products["price"]
    print ("+", name, "({})".format(to_usd(price)))

matching_price = []
for price in matching_products:
    matching_price.append(price["price"])

#SUBTOTAL
for price in matching_products:
    subtotal = subtotal + round(price["price"], 3)
print ("-------------------------------")
print ("Subtotal: ", to_usd(subtotal))


#ROUNDING: 2 decimal places
#https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
tax = subtotal * float(TAX_RATE)   #(input env var here)
tax_cost = round(tax, 3)
#Formatting percentage
#https://www.kite.com/python/answers/how-to-format-a-number-as-a-percentage-in-python
print ("Sales Tax ", "({})".format("{:.2%}".format(float(TAX_RATE))), ": ", to_usd(tax_cost))


#TOTAL PRICE
total = subtotal + tax_cost
print ("Total: ", to_usd(total))
print ("-------------------------------")


#EMAIL RECEIPT
email_choice = input ("Would you wish to receive your receipt by email? 'YES' or 'NO': ")
email_choice = email_choice.upper()
if str(email_choice) == "NO":
    print ("-------------------------------")
    print ("Thanks for your business! Please come again.")
    print ("-------------------------------")

elif str(email_choice) == "YES":
    customer_email = input ("Enter customer email: ")
    template_data = {
        "total_price_usd": to_usd(total),
        "human_friendly_timestamp": date_time,
        "products": matching_products
    } # or construct this dictionary dynamically based on the results of some other process :-D
    message = Mail(
        from_email=SENDER_ADDRESS, 
        to_emails=customer_email,)
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
    print ("-------------------------------")
    print ("Thanks for your business! Please come again.")
    print ("-------------------------------")
