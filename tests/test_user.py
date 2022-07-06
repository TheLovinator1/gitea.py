import pytest
from giteapy.gitea import Gitea
from giteapy.user import User


def test_get_user():
    with Gitea(url=pytest.url, token=pytest.token, log_level="DEBUG") as gitea:
        user = User.get_user(gitea)

        assert hasattr(user, "active")
        assert type(user.active) is bool

        assert hasattr(user, "avatar_url")
        assert type(user.avatar_url) is str

        assert hasattr(user, "created")
        assert type(user.created) is str

        assert hasattr(user, "description")
        assert type(user.description) is str

        assert hasattr(user, "email")
        assert type(user.email) is str

        assert hasattr(user, "followers_count")
        assert type(user.followers_count) is int

        assert hasattr(user, "following_count")
        assert type(user.following_count) is int

        assert hasattr(user, "full_name")
        assert type(user.full_name) is str

        assert hasattr(user, "id")
        assert type(user.id) is int

        assert hasattr(user, "is_admin")
        assert type(user.is_admin) is bool

        assert hasattr(user, "language")
        assert type(user.language) is str

        assert hasattr(user, "last_login")
        assert type(user.last_login) is str

        assert hasattr(user, "location")
        assert type(user.location) is str

        assert hasattr(user, "login")
        assert type(user.login) is str

        assert hasattr(user, "prohibit_login")
        assert type(user.prohibit_login) is bool

        assert hasattr(user, "restricted")
        assert type(user.restricted) is bool

        assert hasattr(user, "starred_repos_count")
        assert type(user.starred_repos_count) is int

        assert hasattr(user, "visibility")
        assert type(user.visibility) is str

        assert hasattr(user, "website")
        assert type(user.website) is str


def test_get_emails():
    with Gitea(url=pytest.url, token=pytest.token, log_level="DEBUG") as gitea:
        emails = User.get_emails(gitea)

        for email in emails:
            assert hasattr(email, "email")
            assert type(email.email) is str

            assert hasattr(email, "verified")
            assert type(email.verified) is bool

            assert hasattr(email, "primary")
            assert type(email.primary) is bool


def test_get_followers():
    with Gitea(url=pytest.url, token=pytest.token, log_level="DEBUG") as gitea:
        followers = User.get_followers(gitea, page=1, limit=10)

        for follower in followers:
            assert hasattr(follower, "active")
            assert type(follower.active) is bool

            assert hasattr(follower, "avatar_url")
            assert type(follower.avatar_url) is str

            assert hasattr(follower, "created")
            assert type(follower.created) is str

            assert hasattr(follower, "description")
            assert type(follower.description) is str

            assert hasattr(follower, "email")
            assert type(follower.email) is str

            assert hasattr(follower, "followers_count")
            assert type(follower.followers_count) is int

            assert hasattr(follower, "following_count")
            assert type(follower.following_count) is int

            assert hasattr(follower, "full_name")
            assert type(follower.full_name) is str

            assert hasattr(follower, "id")
            assert type(follower.id) is int

            assert hasattr(follower, "is_admin")
            assert type(follower.is_admin) is bool

            assert hasattr(follower, "language")
            assert type(follower.language) is str

            assert hasattr(follower, "last_login")
            assert type(follower.last_login) is str

            assert hasattr(follower, "location")
            assert type(follower.location) is str

            assert hasattr(follower, "login")
            assert type(follower.login) is str

            assert hasattr(follower, "prohibit_login")
            assert type(follower.prohibit_login) is bool

            assert hasattr(follower, "restricted")
            assert type(follower.restricted) is bool

            assert hasattr(follower, "starred_repos_count")

            assert hasattr(follower, "visibility")
            assert type(follower.visibility) is str

            assert hasattr(follower, "website")
            assert type(follower.website) is str


def test_get_following():
    with Gitea(url=pytest.url, token=pytest.token, log_level="DEBUG") as gitea:
        following = User.get_following(gitea, page=1, limit=10)

        for user in following:
            assert hasattr(user, "active")
            assert type(user.active) is bool

            assert hasattr(user, "avatar_url")
            assert type(user.avatar_url) is str

            assert hasattr(user, "created")
            assert type(user.created) is str

            assert hasattr(user, "description")
            assert type(user.description) is str

            assert hasattr(user, "email")
            assert type(user.email) is str

            assert hasattr(user, "followers_count")
            assert type(user.followers_count) is int

            assert hasattr(user, "following_count")
            assert type(user.following_count) is int

            assert hasattr(user, "full_name")
            assert type(user.full_name) is str

            assert hasattr(user, "id")
            assert type(user.id) is int

            assert hasattr(user, "is_admin")
            assert type(user.is_admin) is bool

            assert hasattr(user, "language")
            assert type(user.language) is str

            assert hasattr(user, "last_login")
            assert type(user.last_login) is str

            assert hasattr(user, "location")
            assert type(user.location) is str

            assert hasattr(user, "login")
            assert type(user.login) is str

            assert hasattr(user, "prohibit_login")
            assert type(user.prohibit_login) is bool

            assert hasattr(user, "restricted")
            assert type(user.restricted) is bool

            assert hasattr(user, "starred_repos_count")

            assert hasattr(user, "visibility")
            assert type(user.visibility) is str

            assert hasattr(user, "website")
            assert type(user.website) is str
