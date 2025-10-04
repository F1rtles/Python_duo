# lab_2 

print("Завдання №1")

import math

def calculate_function(x):


    if x < 4.5:
        try:
            y = 1 / math.sin(x**2)
        except ZeroDivisionError:
            y = float('inf')
            print(f"Попередження: sin({x**2}) дуже близький до нуля при x={x}. y = Нескінченність")
            
    elif 4.5 <= x < 5:
        try:
            y = x + math.log(math.sqrt(x**7)) 
        except ValueError as e:
            y = "NaN"
            print(f"Помилка: Неможливо обчислити ln/sqrt при x={x}. {e}")
    else: 

        y = math.log10(math.exp(x) + 4) 
        
    return y

def tabulate_function(a, b, h):
    """
    Табулює функцію на проміжку [a, b] з кроком h.
    """
    print("---------------------------------------")
    print(f"Табулювання функції на інтервалі [{a}, {b}] з кроком {h}")
    print("---------------------------------------")
    print("|   x   |      f(x)     |")
    print("---------------------------------------")
    
    x = a

    while x <= b + h/2: 
        y = calculate_function(x)
        

        if isinstance(y, (float, int)):
            print(f"| {x:5.3f} | {y:11.7f}   |")
        else:
            print(f"| {x:5.3f} | {y:11s}   |") 
            
        x += h
        
    print("---------------------------------------")

a = 4.0   
b = 6.0   
h = 0.2   

tabulate_function(a, b, h)