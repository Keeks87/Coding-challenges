'''
Challenge 1

Write a function that doubles every second integer in a list, starting from the
left.

Example:

For input array/list :
[1, 2, 3, 4]

The function should return:
[1, 4, 3, 8]

Feel free to use the language of your choice.
'''


def double_up(given_list):
    '''Function that doubles every second integer in a list'''
    updated_list = []
    # For loop to check index's and manipulate the values
    for i in given_list:
        if i % 2:
            updated_list.append(i)
        else:
            double_number = i * 2
            updated_list.append(double_number)
    return updated_list


# Test case for function
test_list = [1, 2, 3, 4]

# Call the function and display the list in the terminal
print(double_up(test_list))
