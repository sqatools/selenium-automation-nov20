num = 20

#assert num != 20

exp_msg = "Login Succefull"

actual_msg = "login Succefull"

#assert exp_msg == actual_msg, "Test Failed"

list1 = [4, 7, 9, 23, 5, 4]
list2 = [6, 8, 9, 34, 23, 5]

assert 23 in list1, "This number is not available"

dict1 = {'a' : 25, 'b': 30, 'c': 40}

assert 'a' in dict1, "This key is not available in the dict"

assert list1.count(4) == 2, "Number count is not as per expectation"

assert 4 in list1 and 4 in list2, "This number is not in both the list"

