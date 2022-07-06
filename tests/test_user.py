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
