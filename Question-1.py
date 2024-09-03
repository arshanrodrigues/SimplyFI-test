"""
Question 1
Write a python code for converting integer values to Indian currency notations, without
using the currency libraries
Example:
input: 1504678
output: 1,50,467
"""
def currency(n):
    num = str(n)

    # fractions
    if '.' in num:
        int_part, frac_part = num.split('.')
    else:
        int_part, frac_part = num, ''
    
    # last 3 digits
    result = int_part[-3:]
    
    # remaining digits in groups of two
    int_part = int_part[:-3]
    while len(int_part) > 0:
        result = int_part[-2:] + ',' + result
        int_part = int_part[:-2]
    
    # append the fractional part if it exists
    if frac_part:
        result += '.' + frac_part
    
    return result

# Example
input_value = 150467
output_value = currency(input_value)
print(output_value)