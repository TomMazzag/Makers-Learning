class music:

    def __init__(self, name):
        self.name = name
        self.track_list = []

    def add(self, track):
        if len(track) < 1:
            return None
        self.track_list.append(track)

    def show(self):
        if len(self.track_list) < 1:
            return 'No tracks have been added'
        return self.track_list