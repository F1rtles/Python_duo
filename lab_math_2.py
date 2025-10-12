# import math

# a = 4
# b = 6
# h = 0.2
# x = a

# print("Завдання 1")
# print("|   x   |       y       |")

# while x < b + h / 2:
#     if x < 4.5:
#         try:
#             y = 1 / math.sin(x**2) 
#         except ZeroDivisionError:
#             y = float('inf')
#             print(f"| {x:5.3f} | {'Inf.':<11s}    |")
#             x += h
#             continue
    
#     elif x < 5.0:
#          y = x + 3.5 * math.log(x)

#     else:
#         y = math.log10(math.exp(x) + 4)

#     x += h
#     print(f"| {x:5.3f} | {y:11.7f}   |")
    



#/
#/
#/
#/
#/
#/
#/
#/

# import math

# a = 3
# b = 4
# h = 0.1
# d = 0.001
# x = a

# print("Завдання 2")
# print("  x    |     sum(y)")

# while x < b + h / 2:    
#     sum = 0.0
#     k = 1
    
#     while True:
#         task =  1 / k * math.tan(x / 2**k)
#         if abs(task) < d:
#             break   
#         k += 1
#         sum += task

#     x += h    
#     print(f"x: {x:.1f} | y: {sum:.8f}")
    