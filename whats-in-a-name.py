#Task

#Write a function, taking two strings in parameter, that tests whether or not the first string contains all of the letters of the second string, in order.
#The function should return true if that is the case, and else false. Letter comparison should be case-INsensitive.


#solution

def name_in_str(str, name):
    pass # your code here
    # Convert both strings to lowercase for case-insensitive comparison
    str = str.lower()
    name = name.lower()

    # Initialize pointers for both strings
    i = 0  # Pointer for str1
    j = 0  # Pointer for str2

    # Iterate through str1
    while i < len(str):
        # If the current character in str1 matches the current character in str2,
        # move the pointer for str2 to the next character.
        if str[i] == name[j]:
            j += 1
            # If we have matched all characters in str2, return True
            if j == len(name):
                return True
        i += 1

    # If we reach the end of str1 and haven't matched all characters in str2, return False
    return False

# Example usage:
str = "Hello World"
name = "loW"
result = name_in_str(str, name)
print(result)  # Output: True
