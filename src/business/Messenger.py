class Messenger:
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(Messenger, self).__new__(self)
        return self.instance
    
    