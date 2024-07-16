# import the mood_responses module
import mood_responses

# ask the user for input on their mood
mood = input("How are you feeling today? ")

#call the mood_response function from the module and use the users mood
print(mood_responses.mood_response(mood))