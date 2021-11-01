import os

directoryName = ""
while os.path.isdir(directoryName) == False:
    directoryName = input("Please input the directory path.")

txtFileName = input("Please input the file name.")
completeFilePath = directoryName + txtFileName

userName = input("Please enter your name.")
userAddress = input("Please enter your address.")
userPhone = input("Please enter your phone number.")

with open(completeFilePath, 'w') as fileHandle:
    fileHandle.write(directoryName + "\\" + txtFileName + ", " + userName + ", " + userAddress + ", " + userPhone)
with open(completeFilePath, 'r') as fileHandle:
    data = fileHandle.read()
    print(data)