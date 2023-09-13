#Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

#solution
def count_sheep(n):
    # your code
    murmur = ""
    for i in range(1, n + 1):
        murmur += f"{i} sheep..."
    return murmur
