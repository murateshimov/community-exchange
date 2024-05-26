from person import Person


class Partner(Person):
    def __init__(self, username, password, name):
        super().__init__(username, password, name)

    def provide_support(self, new_user):
        # Logic to provide discounts or bonuses to new members
        print(f"Provided support to new user: {new_user}")
