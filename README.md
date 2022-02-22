
# Shopping-Cart

A Completed Repository for the ["Shopping Cart" Project](https://github.com/prof-rossetti/intro-to-python/blob/main/projects/shopping-cart/README.md).

Some descriptions have been adapted from the Tic-Tac-Toe repository, "Command-line Computing" Exercise, and Shopping Cart Project belonging to Professor Rossetti.

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

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

Create .env file:

```sh
touch .env
```

Edit and save a file, using a command-line utility provided by your preferred text editor (like VS Code):

```sh
code .env
```

Create environmental variable within .env file (Example Code):

```sh
# this is the ".env" file... with environment variables

TAX_RATE=0.06
```

NOTE: The ".env" file must be ignored from version control, by using a corresponding entry in the ".gitignore" file.

```sh
# this is the ".gitignore" file...

# ignore environment variables in the ".env" file:
.env
```

## Usage

Configure your own tax rate according to your sales region and run the shopping cart program:

Install python-dotenv to read key-value pairs from a .env file

```sh
pip install python-dotenv
```

Enter tax rate percent as a decimal
```sh
TAX_RATE=0.0875 python shopping_cart.py
```

OR

Continue with default tax rate, 0.06 (D.C. sales tax rate), and run the shopping cart program:

```sh
python shopping_cart.py
```

## Demo

Here is a demonstration of the application:

```
Please input a product identifier, or 'DONE' if there are no more items: 2
Please input a product identifier, or 'DONE' if there are no more items: 3
Please input a product identifier, or 'DONE' if there are no more items: 4
Please input a product identifier, or 'DONE' if there are no more items: done
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
Thanks for your business! Please come again.
-------------------------------

```
