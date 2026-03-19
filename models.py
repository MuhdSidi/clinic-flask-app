from datetime import datetime

class Patient:
    # update 2
    def __init__(self, name):
        self.name = name
        self.time = datetime.now()
    # update 3
    def get_name(self):
        return self.name
    # update 4

    def get_time(self):
        return self.time