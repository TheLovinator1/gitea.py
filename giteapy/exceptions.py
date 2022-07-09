class UserNotFound(Exception):
    """The user was not found."""

    def __init__(self, username: str):
        self.username = username
        super().__init__(f"User {username!r} not found.")


class OAuth2ApplicationNotFound(Exception):
    """The OAuth2 Application was not found."""

    def __init__(self, id: int):
        self.id = id
        super().__init__(f"OAuth2 Application with id {id!r} not found.")


class GPGKeyNotFound(Exception):
    """The GPG Key was not found."""

    def __init__(self, id: int):
        self.id = id
        super().__init__(f"GPG Key with id {id!r} not found.")
