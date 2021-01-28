"""
OS : Modules
"""

import os

"""
# Get all methods in OS module
print(dir(os))

# Get Current Directory Path
cur_path = os.getcwd()
print(cur_path)


# Create folder in current direct

#os.mkdir(cur_path+"//"+'folder1')

# Join path

dir_path = os.path.join(cur_path, 'folder2')
print(dir_path)
#os.mkdir(dir_path)


# Check folder is available if it is there create a file inside it.

foldername = 'folder4'
dir_path2 = os.path.join(cur_path, foldername)
output = os.path.isdir(dir_path2)
print(output)

foldername = 'folder3'
cur_path1 = os.getcwd()
dir_path3 = os.path.join(cur_path1, foldername)

if os.path.isdir(dir_path3):
    print(dir_path3)
    filepath = os.path.join(dir_path3, 'file2.txt')
    with open(filepath, 'w') as file:
        file.write("Hello There")
else:
    os.mkdir(dir_path3)
    print(dir_path3)
    filepath = os.path.join(dir_path3, 'file2.txt')
    with open(filepath, 'w') as file:
        file.write("Hello There")

"""

# Remove directory from path
"""
cur_path4 = os.getcwd()
folderpath = os.path.join(cur_path4, 'folder1')
os.rmdir(folderpath)
"""
# Get list of all files and folder from given path

new_path = 'E:\\BatchNov2020\\Read_Write_Excel\\test_folder'

data_list = os.listdir(new_path)
print(data_list)

print(len(data_list))


"""
# Get count of all different files extension in given path

data_dict = {}
dir_path  = "E:\\BatchNov2020\\Read_Write_Excel\\test_folder"
dir_data = os.listdir(dir_path)

for file in dir_data:
    print(file)
    print(file.split("."))
    file_ext = file.split(".")[1]
    file_name = file.split(".")[0]
    
    if file_ext not in data_dict:
        data_dict[file_ext] = 1
    else:
        data_dict[file_ext] += 1

print(data_dict)

"""

# Program : Get count of files and folder in given

file_dict = {}
dir_list = []
dir_path = "E:\\BatchNov2020\\Read_Write_Excel\\test_folder"
data_list = os.listdir(dir_path)

for data in data_list:
    newpath=  os.path.join(dir_path, data)
    print(newpath)
    if os.path.isdir(newpath):
        dir_list.append(data)
    else:
        ext = data.split(".")[1]
        if ext not in file_dict:
            file_dict[ext] = 1
        else:
            file_dict[ext]  += 1

print(file_dict)
print(dir_list)

