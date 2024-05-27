from person import Person


class Partner(Person):
    def __init__(self, username, password, name):
        super().__init__(username, password, name)

    def provide_support(self, new_user):
        print(f"Provided support to new user: {new_user}")
