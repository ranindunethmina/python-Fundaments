# file1 = open("File Handling\my_file.txt")
# content = file1.readlines()
# print(content, type(content))
# file1.close()

# with open("File Handling\my_file.txt", "r") as file:
#     content = file.read()
#     print(content)
# no need for file.close() as it's automatically handle

with open("File Handling\my_file1.txt", "w") as file:
    file.write("This is awesome.\n")
    file.write("Programming is fun.")


with open("File Handling\my_file2.txt", "w") as file:
    my_list = ["This is something new.\n","This is the writelines method."]
    file.writelines(my_list)