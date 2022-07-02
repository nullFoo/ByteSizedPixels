path = input("file path: ")

newFile = open(path, "wb")

byteArray = bytes([int("00000000", 2), int("10101001", 2), int("11001101", 2), int("01101001", 2)])
newFile.write(byteArray)