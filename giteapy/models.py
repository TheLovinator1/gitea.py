from dataclasses import dataclass


@dataclass
class APIError:
    """APIError is an api error with a message
    # TODO: Add better description of what this is for
    # TODO: Double check the attribute descriptions

    Attributes:
        message: The error message
        url: The url that caused the error
    """

    message: str
    url: str


@dataclass
class AccessToken:
    """AccessToken represents an API access token.
    # TODO: Add better description of what this is for
    # TODO: Double check the attribute descriptions
    # TODO: Make pull request to add a description to the attributes and fix name in swagger?
    """

    id: int
    name: str
    sha1: str
    token_last_eight: str


@dataclass
class ActivityPub:
    """ActivityPub type

    # TODO: Add better description of what this is for
    """

    context: str


@dataclass
class AddCollaboratorOption:
    """AddCollaboratorOption options when adding a user as a collaborator of a repository

    # TODO: Add better description of what this is for
    """

    permission: str


@dataclass
class AddTimeOption:
    """AddTimeOption options for adding time to an issue

    # TODO: Check why star after time
    # TODO: Add better description of what this is for
    # TODO: created and last_login is a string, but it should be a datetime ("created": "2022-07-06T14:33:25.419Z")
    """

    created: str
    time: int
    user_name: str


@dataclass
class UserModel:
    """User represents a user on Gitea.

    Attributes:
        active: Is the user active?
        avatar_url: URL to the user's avatar.
        created: When the user was created.
        description: The user's description.
        email: The user's email.
        followers_count: The number of followers.
        following_count: The number of users the user follows.
        full_name: The user's full name.
        id: The user's ID.
        is_admin: Is the user an administrator?
        language: The user locale.
        last_login: The last time the user logged in.
        location: The user's location.
        login: The user's username.
        prohibit_login: Is the user prohibited from logging in?
        restricted: Is the user restricted?
        starred_repos_count: The number of starred repos.
        visibility: The user's visibility. (public, limited, private)
        website: The user's website.

    # TODO: created and last_login is a string, but it should be a datetime ("created": "2022-07-06T14:33:25.419Z")
    """

    active: bool
    avatar_url: str
    created: str
    description: str
    email: str
    followers_count: int
    following_count: int
    full_name: str
    id: int
    is_admin: bool
    language: str
    last_login: str
    location: str
    login: str
    prohibit_login: bool
    restricted: bool
    starred_repos_count: int
    visibility: str  # public, limited, private
    website: str


@dataclass
class EmailListModel:
    """Email an email address belonging to a user

    # TODO: Add better description of what this is for

    Attributes:
        email: The email address
        primary: Is this the primary email address?
        verified: Is the email address verified?
    """

    email: str
    primary: bool
    verified: bool
