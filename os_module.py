import os

# print(os.__file__)
# os.mkdir("collections")
cwd = os.getcwd()
print(cwd)

# directory = "data"
# parent_dir = (r"C:\Upendra\Python")
# path = os.path.join(parent_dir,directory)
# os.mkdir(path)

# path = (r"C:\Upendra\Python\data")
# dir_list = os.listdir(path)
# print(dir_list)

file = "data"
location = (r"C:\Upendra\Python")
path = os.path.join(location,file)
os.rmdir(path)