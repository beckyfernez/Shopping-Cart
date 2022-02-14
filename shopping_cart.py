

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


while True:

    #ASK FOR USER INPUT
    product_id = input ("Please input a product identifier, or 'DONE' is there are no more items: ")
    #print(product_id)
    #print(type(product_id))

    #VALIDATE USER INPUT
    #https://www.datasciencemadesimple.com/lower-upper-title-function-python/
    product_id = product_id.upper()

    #EXIT CODE WHEN FINISHED
    if product_id == "DONE":
        break
    
    #STORE SELECTED ITEMS INTO NEW LIST
    else:
        selected_ids.append(product_id)

#print (selected_ids) (e.g. ['4', '5'])


#LOOK UP & RETURN CORRESPONDING PRODUCTS IN NEW LIST
for product_id in selected_ids:
    for id in products:
        if str(id["id"]) == str(product_id):
        #this is a match using string conversion since the list uses integers
            matching_products.append(id)
            #print(matching_products)
    matched_product = matching_products[0] #(0 = the placement of the item in the list?)
    subtotal = subtotal + matched_product["price"] #this is an int
    #print (matched_product["name"], " (", to_usd(matched_product["price"]), ")")


print ("-------------------------------")
print ("COBRA GROCERY")
print ("-------------------------------")
print ("Website: www.cg.com")
print ("Phone: 202.687.5874")
print ("Checkout Time: ")
print ("-------------------------------")
print ("Shopping Cart Items: ")


for products in matching_products:
    name = str(products["name"])
    price = products["price"]
    print ("+", name, " (", to_usd(price), ")")


print ("-------------------------------")
print ("Subtotal: ", to_usd(subtotal))
print ("DC Sales Tax: ")
print ("Total: ")
print ("-------------------------------")
print ("Thanks for your business! Please come again.")


# TODO ---a grocery name of your choice
#      ---a grocery store phone number, website URL, address
#      -date and time of the beginning of the check out process
#      ---name and price of each shopping cart item (format USD and cents (float or double))
#      ---total cost of all items (format USD and cents)
#      -the amount of tax owed (multiply total cost by DC's tax rate)
#      -total amount owed (format USD and cents, add total tax and cost)
#      ---message thanking the customer and encouraging the customer to shop again
