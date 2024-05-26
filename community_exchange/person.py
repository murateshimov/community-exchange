# Person class - base class for all roles  

class Person:
    def __init__(self, username, password, name):
        self.username = username
        self.password = password
        self.name = name

    def get_details(self):
        return {
            "username": self.username,
            "name": self.name
        }