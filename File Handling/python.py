# file1 = open("File Handling\my_file.txt")
# content = file1.readlines()
# print(content, type(content))
# file1.close()

with open("File Handling\my_file.txt", "r") as file:
    content = file.read()
    print(content)
# no need for file.close() as it's automatically handle