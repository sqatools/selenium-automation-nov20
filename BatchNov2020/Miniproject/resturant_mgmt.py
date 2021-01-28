employee_list = []
food_item = []
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
        emp_name = input("Enter Employee Name :")
        emp_age  = input("Enter Employee Age :")
        emp_salary = input("Enter Employee Salary :")

        employee_list.append([emp_name, emp_age, emp_salary])

    elif userinput == 2:
        emp_name = input("Enter Employee Name to Remove:")
        if employee_list == []:
            print("There is no employee in the list")
        else:
            for emp in employee_list:
                if emp_name in emp:
                    employee_list.remove(emp)
                    print("Entry removed successfully")
                    break
                else:
                    continue

    elif userinput == 3:
        for data in employee_list:
            print(f"Name :{data[0]} | Age : {data[1]} | Salary : {data[2]}")

    elif userinput == 4:
        item_name = input("Please enter Food Item Name:")
        item_price = input("Please enter Item Price")
        food_item.append([item_name, item_price])

    elif userinput == 5:
        item_name = input("Please enter Food Item Name:")
        for item in food_item:
            if item_name == item[0]:
                food_item.remove(item_name)
                break
            else:
                continue
    elif userinput == 6:
        for item in food_item:
            print(f"{item[0]}  : {item[1]}")

    print("\n")
    print("\n")
    print("*"*50)