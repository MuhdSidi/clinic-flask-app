from datetime import datetime

class Patient:
    # update 2
    def __init__(self, name):
        self.name = name
        self.time = datetime.now()

    def get_name(self):
        return self.name

    def get_time(self):
        return self.time