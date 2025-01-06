# 1st way
# import my_calculator.addition
# import my_calculator.subtraction

# result1 = my_calculator.addition.add(3,4)
# result2 = my_calculator.subtraction.subtract(7,3)

# print(result1,result2)

# 2nd way
# from my_calculator import addition
# from my_calculator import subtraction

# result1 = addition.add(3,4)
# result2 = subtraction.subtract(7,3)

# print(result1,result2)

# 3rd way
# from my_calculator.addition import add
# from my_calculator.subtraction import subtract

# result1= add(3,4)
# result2= subtract(7,3)

# print(result1,result2)

from my_calculator import add,subtract

result1 = add(3,4)
result2 = subtract(7,3)

print(result1,result2)