a = 30
b = 40
c = 50

def print_table(num):
    for i in range(11):
        print(f"{i}*{num} = {i*num}")


def open_fun10line1(file_path,file_path1):
    with open(file_path, 'r') as file:
        with open(file_path1,'a') as file1:
            for i in range(1, 10):
                filedata = file.readline()
                file1.write(filedata)
                print(filedata)

file_path="my1.txt"
file_path1="my2.txt"
open_fun10line1(file_path, file_path1)
