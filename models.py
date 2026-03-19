
from datetime import datetime

class Patient:

    # update
    def __init__(self, name):
        self.name = name
        self.time = datetime.now()

    # update
    def get_name(self):
        return self.name
    
    # update
    def get_time(self):
        return self.time