import re

class contacts():

    def __init__(self, entries):
        self.entries = entries

    def findContacts(self):
        numbers = []
        for content in self.entries.values():
            numbers += re.findall(r"0[0-9]{10}", content)
        return numbers