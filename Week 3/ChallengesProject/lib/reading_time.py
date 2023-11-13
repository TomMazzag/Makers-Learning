def estimated_reading_time(text):
    words_per_minute = 200
    words_per_second = words_per_minute / 60
    words_in_string = len(text.split())
    minutes = words_in_string // words_per_minute
    seconds = round((words_in_string % words_per_minute) / words_per_second)
    time_string = 'Estimated reading time: '
    if minutes == 1:
        time_string += f'{minutes} minute'
        if seconds > 0:
            time_string += f' and {seconds} seconds'
    elif minutes > 1:
        time_string += f'{minutes} minutes'
        if seconds > 0:
            time_string += f' and {seconds} seconds'
    else:
        time_string += f'{seconds} seconds'

    if words_in_string == 0:
        return('No words in input')
    
    return(time_string)

