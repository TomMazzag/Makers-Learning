class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.word_list = []
        self.start = 0
        self.end = 0
        self.chunk = ''

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        words = self.title + " " + self.contents
        self.word_list = words.split()
        return len(self.word_list)

    def reading_time(self, wpm):
        minutes = self.count_words() / wpm
        return round(minutes)

    def reading_chunk(self, wpm, minutes):
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        total_words = wpm * minutes
        self.end += total_words
        self.count_words()
        for word in self.word_list[self.start:self.end]:
            self.chunk += f"{word} "
        self.start = total_words
        return self.chunk