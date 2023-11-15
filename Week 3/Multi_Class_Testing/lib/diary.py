
class diary():

    def __init__(self):
        self.entries = {}
        self.contacts = []

    def add_entry(self, title, contents):
        self.entries[title] = contents
        return title, contents

    def show_all(self):
        return self.entries

    def read(self, title):
        return self.entries[title]
    
    def read_in_time(self, time, words_per_minute):
        readable = []
        for title, content in self.entries.items():
            if len(content.split()) <= time * words_per_minute:
                readable.append(title)
        return readable
