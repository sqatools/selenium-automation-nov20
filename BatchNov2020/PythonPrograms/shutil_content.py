import shutil
import os
src = 'E:\\Filesdata\\xls'
tar = 'E:\\Filesdata\\copyfiles'

listdir = os.listdir(src)
for file in listdir:
    filepath = os.path.join(src, file)
    shutil.copy(filepath, tar)

#################################
target_path = 'E:\\Filesdata'
new_path = 'E:\\Filesdata'

for i in range(1, 10):
    new_path = os.path.join(new_path, str(i))
    os.mkdir(new_path)
    filepath = os.path.join(new_path, str(i)+".txt")
    with open(filepath, 'w') as file:
        file.write("Hello this is python")






