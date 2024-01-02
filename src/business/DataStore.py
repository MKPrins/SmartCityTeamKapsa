class DataStore:

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(DataStore, self).__new__(self)
        return self.instance
    
    def __init__(self):
        self.__data = {
            "temperature": 0.0,
            "humidity": 0.0
        }
    
    def setData(self, key: str, value: int):
        self.__data[key] = value

    def getData(self, key: str):
        return self.__data[key]
    