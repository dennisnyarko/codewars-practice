"""
Question

Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
Examples (Input -> Output):

* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "

"""
#solution

def double_char(s):
    duplicate_string = ""
    for arr in s:
        duplicate_string += arr*2
    return duplicate_string
    
