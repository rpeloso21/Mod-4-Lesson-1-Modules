

def mood_response(mood):
    good_moods = ["happy", "glad", "excited", "energetic", "fantastic", "good"]
    neutral_moods = ["alright", "ok", "okay", "fine"]
    bad_moods = ["bad", "sad", "upset", "depressed", "negative", "pessimistic", "down"]

    if mood.lower() in good_moods:
        return("I'm glat that you are in a good mood today.  Life is going to bring you all of the joy that you are expecting!!!  Go get the day!")

    elif mood.lower() in neutral_moods:
        return("Things could be worse, and it is a new day.  Go out and make this day whatever you want it to be!")

    elif mood.lower() in bad_moods:
        return(f"I'm sorry that you are not feeling great today.  I know that you are feeling {mood}, but everyone has these kind of days and you never know what will happen next.  This too will pass.")
    
    else:
        return(f"Sometimes I feel {mood} too.  I'm glad that we have a wide range of emotions and that no one is a machine!... except for me of course.")