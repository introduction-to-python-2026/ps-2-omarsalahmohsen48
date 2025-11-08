import math

print("enter 3 numbers")

num1 = int(input())
num2 = int(input())
num3 = int(input())

# The biggest number
def find_max_number(num1, num2, num3):
    max_num = max(num1, num2, num3)
    return max_num

#The avrige
def find_mean(num1, num2, num3):
    avr_num = (num1 + num2 + num3) / 3
    return avr_num
    
# the Standard Deviation (std)? sorry but i had to look ask chatgpt for this monstrosty of a formila

def find_mean_std(num1, num2, num3):
    avr_num = (num1 + num2 + num3) / 3
    variance = ((num1 - avr_num) ** 2 + (num2 - avr_num) ** 2 + (num3 - avr_num) ** 2) / 3
    std = math.sqrt(variance)
    return std
    
    
print(find_max_number(num1, num2, num3))
print(find_mean(num1, num2, num3))
print(find_mean_std(num1, num2, num3))
