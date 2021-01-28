"""
Mini Project :

7. Create python script to manage fruit shop.
1. Fruit_quantity : {'apple' : 50, 'mango':100, 'pineapple' : 60}
2. Fruit Price : {'apple' : 200, 'mango': 300, 'pineapple' : 400}}
3. Create a bill as per user requirement and maintain inventory as well.

e.g user get 5 apple, then total bill will be 5*200 = 1000 and remain apples will be 45.

Shop_management_option
1. Add Inventory
2. Check Inventory
3. Total Purchase or Sold Item
4. Generate Bill
5. Total profit

"""

fruit_quantity = {}
fruit_price = {}
fruit_profit = {}
total_sold_item = {}

def get_fruit_inventory(**kwargs):
    return kwargs

def get_fruit_price(**kwargs):
    return kwargs

fruit_quantity =  get_fruit_inventory(apple=100, mango=200, pipeapple=400)
fruit_price    =  get_fruit_price(apple=50, mango=20, pipeapple=40)

def show_menu():
    for k, v in fruit_price.items():
        print("Fruit:", k ," Price :",v)

def take_order():
    show_menu()
    fruit_name = input("Please select your fruit :")
    fruit_qua  = int(input("Please provide your fruit unit :"))
    return fruit_name, fruit_qua

def generate_bill():
    fruit, f_qua =  take_order()
    price = fruit_price[fruit]
    total_bill = f_qua*price
    print("*"*10, "Total Bill", "*"*10)
    print("Please pay following bill amount for :", fruit)
    print("Total Bill :", total_bill)

generate_bill()





