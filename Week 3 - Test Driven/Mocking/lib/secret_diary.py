class SecretDiary:
    def __init__(self, diary):
        self.diary = diary
        self.locked = False

    def read(self):
        # Raises the error "Go away!" if the diary is locked
        # Returns the diary's contents if the diary is unlocked
        # The diary starts off locked
        
        if self.locked == True:
            raise Exception('Go Away!')
        return self.diary

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False