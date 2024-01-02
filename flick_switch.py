"""
Question
Create a function that always returns true for every item in a given list. However, if an element is the word "flick", switch to always returning the opposite boolean value.

Examples

['codewars', 'flick', 'code', 'wars'] ➞ [True, False, False, False]

['flick', 'chocolate', 'adventure', 'sunshine'] ➞ [False, False, False, False]

['bicycle', 'jarmony', 'flick', 'sheep', 'flick'] ➞ [True, True, False, False, True]

"""

#SOLUTION
def flick_switch(input_list):
    switch = True  # Start with True, as the first element is not 'flick'
    result = []

    for item in input_list:
        if item == 'flick':
            switch = not switch
        result.append(switch)

    return result

# Examples
print(flick_switch(['codewars', 'flick', 'code', 'wars']))  # ➞ [True, False, False, False]
print(flick_switch(['flick', 'chocolate', 'adventure', 'sunshine']))  # ➞ [False, False, False, False]
print(flick_switch(['bicycle', 'jarmony', 'flick', 'sheep', 'flick']))  # ➞ [True, True, False, False, True]



#REFACTORED SOLUTION
# def flick_switch(lst):
# 	res, state = [], True
# 	for i in lst:
# 		if i == 'flick':
# 			state = not state
# 		res.append(state)
# 	return res
