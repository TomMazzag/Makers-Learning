class GrammarStats:
    def __init__(self):
        self.passed = 0
        self.total = 0
        pass
  
    def check(self, text):

        if len(text) == 0:
            return False
        
        if text[0].isupper() and text[-1] in '.!?':
                self.total += 1
                self.passed += 1
                return True
        elif text[0].isupper():
                self.total += 1
                return False
        self.total += 1
        return False
  
    def percentage_good(self):
        if self.total == 0:
             return 'No strings tested'
        percent = int((self.passed / self.total) * 100)
        return f"{percent}%"