class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        removed = ''
        while i < len(self.text):
            if self.text[i].lower() in self.vowels:
                i += 1
                continue
            else:
                removed += self.text[i]
            i += 1
            
        return removed
    
#remover = VowelRemover("testaeiou")
#result_no_vowels = remover.remove_vowels()
#print(result_no_vowels)
