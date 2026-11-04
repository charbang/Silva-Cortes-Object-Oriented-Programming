class user:
    def __init__(self, id_user, name):
        self.id = id_user
        self.name  = name
        # list of book ids borrowed by this user
        self.borrowed = []

    def show_user_info(self):
        return f"ID: {self.id}\n- {self.name}\n- Borrowed: {len(self.borrowed)}\n"