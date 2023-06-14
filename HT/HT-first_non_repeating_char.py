def first_non_repeating_char(string):
    l_count = {}
    for char in string:
        l_count[char] = l_count.get(char, 0)+1
    for char in string:
        if l_count[char] == 1:
            return char
    return None

print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""