
file_name = "file1.txt"

# To write in the file
file = open(file_name,'w')
file.write("Hello world")
file.close()

#To read the file content
file = open(file_name,'r')
file_text = file.read()
print(file_text)
file.close()

# To readlines in a file
file = open(file_name,'r')
while True:
    line=file.readline()
    if not line:
        break
    print(line)

# To Write lines on the file
file = open(file_name,'w')
lines=["Hello world1\n","Hello world2\n","Hello world3\n",]
file.writelines(lines)
file.close()