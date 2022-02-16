
# Shopping-Cart

A Completed Repository for the ["Shopping Cart" Project](https://github.com/prof-rossetti/intro-to-python/blob/main/projects/shopping-cart/README.md).

Some descriptions have been adapted from the tic-tac-toe repository belonging to Professor Rossetti.

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
conda create -n rps-env python=3.8
```

Activate the virtual environment:

```sh
conda activate rps-env
```

Install package dependencies (mainly for testing):

```sh
pip install -r requirements.txt
```

## Usage

```sh
python shopping_cart.py
```

## Demo

Here is a demonstration of the application:

```
Please input a product identifier, or 'DONE' if there are no more items: 1
Please input a product identifier, or 'DONE' if there are no more items: 2
Please input a product identifier, or 'DONE' if there are no more items: 3
Please input a product identifier, or 'DONE' if there are no more items: DONE
-------------------------------

processing receipt...

-------------------------------
COBRA GROCERY
-------------------------------
Website: www.cg.com
Phone: 202.687.5874
Checkout Time:  2022-02-14 00:21:27.439139-05:00
-------------------------------
Shopping Cart Items:
+ Chocolate Sandwich Cookies  ( $3.50 )
+ All-Seasons Salt  ( $4.99 )
+ Robust Golden Unsweetened Oolong Tea  ( $2.49 )
-------------------------------
Subtotal:  $10.50
DC Sales Tax (6%):  $0.63
Total:  $11.13
-------------------------------
Thanks for your business! Please come again.
```
