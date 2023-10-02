"""
Question
Complete the function which converts a binary number (given as a string) to a decimal number.
"""

#solution

def bin_to_decimal(inp):
    try:
        decimal_num = int(inp, 2)
        return decimal_num
    except ValueError:
        return "Invalid binary input"
