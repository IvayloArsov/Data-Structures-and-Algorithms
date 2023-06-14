def find_longest_string(myList):
    longest = ""
    for element in myList:
        if len(element) > len(longest) :
            longest = element
    return longest


string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  


"""
    EXPECTED OUTPUT:
    ----------------
    banana
    
"""