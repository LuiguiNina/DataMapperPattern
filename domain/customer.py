class Customer:
    def __init__(self, id=None, name="", email=""):
        self.id = id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<Customer id={self.id}, name='{self.name}', email='{self.email}'>"