class UserNotFound(Exception):
    """The user was not found."""

    def __init__(self, username: str):
        self.username = username
        super().__init__(f"User {username!r} not found.")
