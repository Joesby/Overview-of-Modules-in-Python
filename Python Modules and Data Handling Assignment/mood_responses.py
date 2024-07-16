#create two lists for positive moods and negative moods
positive_moods = ["happy", "excited", "joyful", "ecstatic", "peaceful"]
negative_moods = ["sad", "angry", "anxious", "worried", "upset"]

# define a mood_response function
def mood_response(mood):
    # provide feedback for positive moods
    if mood.lower() in positive_moods:
        response = "I'm glad you're having a good day!"
    # provide feedback for negative moods
    elif mood.lower() in negative_moods:
        response = "I'm sorry, I hope your day gets better soon!"
    # use a catch-all feedback for anything not in the positive and negative lists
    else:
        response = "Human emotions are complicated, aren't they?"

    # return a response to be printed when the function is called
    return response