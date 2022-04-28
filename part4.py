from operator import truediv
from pickle import FALSE


def max_num(int, int2, int3):
    return max([int, int2, int3])

print(max_num(3, 6, 8))

def mult_list(list):
    product = list[0]
    
    for i in range(len(list)):
        product = product * list[i]
        
    return product

print(mult_list([1, 5, 10]))
print(mult_list([0, 6, 6]))

def reverse_string(str):
    return str[::-1]

print(reverse_string("how are you today?"))

def num_within(num, range_start, range_end):
    return num in range(range_start, range_end + 1)
        
num_within(5, 1, 5)

triangle=[[1], [1,1]]

def pascal(n):
    if n < 1:
        print("invalid number of rows")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]
            length = len(row_prev) + 1
            for i in range(length):
                if i == 0 :
                    row.append(1)
                elif i > 0 and i < length - 1:
                    row.append(triangle[row_number - 1][i - 1] + triangle[row_number - 1][i])
                else:
                    row.append(1)
                    
            triangle.append(row)
            row_number += 1
            
        for row in triangle:
            print(row)
            
pascal(2)
pascal(7)