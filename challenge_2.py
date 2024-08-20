'''
Challenge 2

The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

* It must start with a hashtag (#).
* All words must have their first letter capitalized.
* If the final result is longer than 140 chars it must return false.
* If the input or the result is an empty string it must return false.

Example
" Hello there thanks for joining"  =>  "#HelloThereThanksForJoining"
"    Hello     World   "           =>  "#HelloWorld"
""                                 =>  false
'''


def generate_hashtag(user_string):
    '''Function that generates hashtags by taking in a users string'''
    # Check if the string is empty
    if user_string != "":
        # Split the words into a list
        user_words = user_string.split()
        # Use capitalize for each word in the list and join the string
        final_string = "#" + "".join(word.capitalize() for word in user_words)
        # Check if the string is longer than 140 characters
        if len(final_string) > 140 or len(final_string) == 0:
            return False
        else:
            print(final_string)
    else:
        return False


# Get the string from the user
user_input_string = input("Please enter the sentence you want to edit:")
print(generate_hashtag(user_input_string))
