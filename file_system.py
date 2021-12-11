import os.path

# prompt user for the directory and file name as user input
directoryName = input("Please enter the name of the directory: ")
if (os.path.isdir(directoryName) == False):
    os.mkdir(directoryName)

fileName = input("Please enter the name of the file: ")

filePath = os.path.join(directoryName, fileName)

# Will open the file if it exists, or will create a new one
file_1 = open(filePath, 'a')

# prompt user for username, address, and phone number
fileObject = open(filePath, "w")
name = input("Please enter your name: ")

address = input("Please enter your address: ")

phone = input("Please enter your phone number: ")

fileObject.write(name + "," + "" + address + "," + "" + phone + "\r")
fileObject.close()

fileObject = open(filePath, "r")
print(fileObject.read())


