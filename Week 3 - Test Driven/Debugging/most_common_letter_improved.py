def get_most_common_letter(text):
    counter = {}
    for char in text:
        if char.isalpha():
            counter[char] = counter.get(char, 0) + 1
        #print(counter)
    letter = max(counter.items(), key=lambda item: item[1])
    #print(sorted(counter.values(), reverse=True))
    #print()
    return letter[0]

print(get_most_common_letter("the roof, the roof, the roof is on fire!"))