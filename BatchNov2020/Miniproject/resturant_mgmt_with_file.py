from PythonPrograms.FilePrograms import *

employee_details_file = 'employee_data.txt'
food_menu_item_file = 'foodmenu.txt'

while True:
    print("1. Add Employee \n"
          "2. Remove Employee \n"
          "3. Show Employee Details \n"
          "4. Add Food Item \n"
          "5. Remove Food Item \n"
          "6. Food Menu \n"
          )

    userinput = int(input("Please select your option :"))

    if userinput == 1:
        name = input("Enter Employee Name :")
        age  = input("Enter Employee Age :")
        salary = input("Enter Employee Salary :")
        Address = input("Enter Employee Address :")
        store_employee_data('employee_details.txt', name=name, age=age, salary=salary, address=Address)


    elif userinput == 2:
        emp_id = int(input("Enter Employee ID to Remove:"))
        #import pdb; pdb.set_trace()
        # s =
        remove_employee_detail(emp_id, filepath='employee_details.txt')

    elif userinput == 3:
        emp_id = int(input("Enter Employee ID to get details:"))
        get_employee_details(emp_id, filepath='employee_details.txt')

    # elif userinput == 4:
    #     item_name = input("Please enter Food Item Name:")
    #     item_price = input("Please enter Item Price")
    #     food_item.append([item_name, item_price])
    #
    # elif userinput == 5:
    #     item_name = input("Please enter Food Item Name:")
    #     for item in food_item:
    #         if item_name == item[0]:
    #             food_item.remove(item_name)
    #             break
    #         else:
    #             continue
    # elif userinput == 6:
    #     for item in food_item:
    #         print(f"{item[0]}  : {item[1]}")
    #
    # print("\n")
    # print("\n")
    # print("*"*50)