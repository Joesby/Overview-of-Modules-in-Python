#import the text_utils module with an alias
import text_utils as text

#request user input to use in the functions
user_input = input("Please enter some text: ")

# display the result of calling each function in the module using the alias
print(text.reverse_string(user_input))
print(text.capitalize_string(user_input))