# define a function for reversing a string 
def reverse_string(s):
    # create a list store characters from a string
    reverse_list = []
    # assign a variable with the length of the given string
    i = len(s)

    # iterate through the string starting from the last character 
    while i > 0:
        # add each character to the list and decrement the iterable
        reverse_list.append(s[i - 1])
        i -= 1

    # join the reversed list into a string
    s = "".join(reverse_list)

    # return the new string
    return s

# define a function that capitalizes a string
def capitalize_string(s):
    string_list = []

    # iterate through the given string
    for i in s:
        # add each character of the string to the string list
        string_list.append(i)

    # change the first item in the list to uppercase
    string_list[0] = string_list[0].upper()

    # join the list back into a string
    s = "".join(string_list)

    # return the new string
    return s