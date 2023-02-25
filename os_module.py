import os

print(os.__file__)
if not os.path.exists("collections"):
    os.mkdir("collections")
cwd = os.getcwd()
print(cwd)

directory = "data"
parent_dir = (r"C:\Upendra\Python")
path = os.path.join(parent_dir,directory)
if not os.path.exists(path):
    os.mkdir(path)

path = (r"C:\Upendra\Python\data")
dir_list = os.listdir(path)
print(dir_list)

file = "data"
location = (r"C:\Upendra\Python")
path = os.path.join(location,file)
if os.path.exists(path):
    os.rmdir(path)

print(os.name)

# size = os.path.getsize("collections")

for i in range (0,100):
    if not os.path.exists(f"collections/data{(i)}"):
        os.mkdir(f"collections/data{(i)}")
size = os.path.getsize("collections")
print(size)

os.removedirs(r"C:\Upendra\Python\collections")