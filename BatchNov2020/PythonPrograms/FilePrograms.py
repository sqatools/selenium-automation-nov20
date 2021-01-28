# Program : Get count of given word in a file

def get_count_of_name_file(filepath, input):

    with open(filepath, 'r') as file:
        data = file.read()
        totalcount = data.count(input)
        print(totalcount)


filepath = 'C:\\Testdata\\count_name.txt'
input_word = 'SQATools'
#get_count_of_name_file(filepath, input_word)


# Program : Print all lines where specified word is available

def print_lines(filepath, input):
    with open(filepath, 'r') as file:
        all_lines = file.readlines()

    for line in all_lines:
        if input in line:
            print("\n", line)
            print("\n", line.count(input))  # give total count

            for word in line.split(" "): # print particular in a given line
                if word.lower() == input.lower():
                    print(word, end=' ')
                else:
                    continue
        else:
            continue

filepath = 'C:\\Testdata\\count_name.txt'
input_word = 'SQAToolS'
#print_lines(filepath, input_word)


# Gel all line from file1 which has matching words of list and put in file2
wordlist = ['SQATools', 'Learning', 'Automation', 'Python']

def get_lines(wordlist, file1, file2):

    with open(file1, 'r') as file:
        # Get all lines of file1
        all_lines = file.readlines()

        # Open second file to insert/append data
        with open(file2, 'a') as file2:

            # Loop through each lines
            for line in all_lines:

                # loop through each word which is given
                for word in wordlist:
                    if word in line:
                        file2.write(line)
                        continue
                    else:
                        continue



file1 = "C:\\Testdata\\get_line_file1.txt"
file2 =  "C:\\Testdata\\get_line_file2.txt"
#get_lines(wordlist, file1, file2)

####################################################################
# Program : Replace your name with surname in the file and put in another file.

file1 = "C:\\Testdata\\replace_content.txt"
file2 = "C:\\Testdata\\replace_content2.txt"


def replace_content(filepath1, filepath2):

    with open(filepath1, 'r') as file1:
        file1data = file1.readlines()

    with open(filepath2, 'a') as file2:

        for line in file1data:
            if 'SQATools' in line:
                data = line.replace('SQATools', 'Learning')
                file2.write(data)
            else:
                file2.write(line)

#replace_content(file1, file2)

def replce_inside_file(filepath):
    with open(filepath, 'r') as file:
        filedata = file.read()


    with open(filepath, 'w') as file1:
        newdata = filedata.replace("SQATools", "Selenium")
        file1.write(newdata)

#replce_inside_file(file1)

def get_input_from_file(filepath):
    with open(filepath, 'r') as file:
        filedata = file.readlines()

        for line in filedata:
            if 'name' in line:
                print("name:", line.split(":")[1])
            elif 'address' in line:
                print("address:", line.split(":")[1])
            elif 'salary' in line:
                print("salary:", line.split(":")[1])
            elif 'age' in line:
                print("age:", line.split(":")[1])


filepath = 'C:\\Testdata\\userinput.txt'
#get_input_from_file(filepath)


def store_employee_data(filepath, **kwargs):
    print(kwargs)
    with open(filepath, 'r') as fileobj:
        last_line = fileobj.readlines()
        if last_line == []:
            last_id = 100
            newid = last_id
        else:
            last_id = last_line[-1].split("=")[0]
            print(last_id)
            newid = int(last_id)+1
            print(newid)

    with open(filepath, 'a') as fileobj:
        content = f'\n{newid}={kwargs}'
        fileobj.write(content)


filepath1 = 'C:\\Testdata\\employee_details.txt'
#store_employee_data(filepath1, name='Chetana', address='Hyderbad', age=25, salary=10000)
#store_employee_data(filepath1, name='Sagar', address='Pune', age=20, salary=11000)
#store_employee_data(filepath1, name='Priya', address='Pune', age=20, salary=12000)
#store_employee_data(filepath1, name='Smita', address='Pune', age=25, salary=13000)
#store_employee_data(filepath1, name='Ambika', address='Hyderabad', age=25, salary=15000)



def get_employee_details(empl_id, filepath='C:\\Testdata\\employee_details.txt'):
    with open(filepath, 'r') as file:
        filedata = file.readlines()

        for line in filedata:
            linedata = line.split("=")
            #print(linedata)
            if int(linedata[0]) == empl_id:
                #print(line)
                print(linedata[1])


#get_employee_details(5)

def remove_employee_detail(empl_id, filepath="C:\\Testdata\\employee_details.txt"):
    updated_data = []
    with open(filepath, 'r') as file:
        filedata = file.readlines()

        for line in filedata:
            linedata = line.split("=")
            #print(linedata)
            #print(line)
            if int(linedata[0]) == empl_id:
                continue
            else:
                updated_data.append(line)

    data_str = ''
    for data in updated_data:
        data_str = data_str + data

    with open(filepath, 'w') as file:
        file.write(data_str)


#remove_employee_detail(103)