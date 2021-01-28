import shutil
import os
# copy file from one folder to another
"""
folder3 = os.path.join(os.getcwd(), 'folder3')
folder2 = os.path.join(os.getcwd(), 'folder2')
src_filepath = os.path.join(folder3, 'file1.txt')
tag_filepath = os.path.join(folder2, 'file1.txt')

shutil.copy(src_filepath, tag_filepath)

src = "E:\\BatchNov2020\\Modules\\folder3\\file2.txt"
dest = "E:\\BatchNov2020\\Modules\\folder2\\file2.txt"

shutil.copy(src, dest)


# Remove folder
shutil.rmtree("E:\\BatchNov2020\\Modules\\folder3")
"""

# copy all type of files from one location another in specified folder

def copy_dff_ext_files():
    # Root Directory
    root_dir = "C:\\Testdata"
    root_dir2 = "E:\\Filesdata"

    # Target Directory, from where will pick data
    target_dir = os.path.join(root_dir, 'test_folder')

    # Get list of data from  target directory
    dire_data = os.listdir(target_dir)

    # Apply loop in list of files and folders
    for data in dire_data:
        print(data)

        # get path of each files and folder
        datapath = os.path.join(target_dir, data)

        # Check given data is folder/directory
        if os.path.isdir(datapath):
            continue

        else:
            # In else condition the data is file
            # Get extension of file
            ext = data.split(".")[1]

            # get path of extension folder/directory
            ext_dire_path = os.path.join(root_dir2, ext)

            # check if extension folder is already available
            if os.path.isdir(ext_dire_path):
                src_path = datapath
                des_path = os.path.join(ext_dire_path, data)

                # copy file from target to extension folder
                shutil.copy(src_path, des_path)
            else:
                # Create extension folder if it is not there in root directory
                os.mkdir(ext_dire_path)

                src_path = datapath
                des_path = os.path.join(ext_dire_path, data)

                # copy file from target to extension folder
                shutil.copy(src_path, des_path)


copy_dff_ext_files()


