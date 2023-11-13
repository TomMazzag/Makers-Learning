def grammar(text):

    if len(text) == 0:
        return 'Invalid, no text given'
    
    if text[0].isupper() and text[-1] in '.!?':
            return 'Grammar is correct'
    elif text[0].isupper():
            return 'Missing punctuation'
    
    return 'Missing capital letter at the start'