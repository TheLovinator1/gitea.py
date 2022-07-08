import pytest
from giteapy.gitea import Gitea
from giteapy.user import User
from giteapy.exceptions import UserNotFound


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


def test_if_following():
    with Gitea(url=pytest.url, token=pytest.token, log_level="DEBUG") as gitea:
        if_following_lovibot = User.if_following(gitea, "LoviBot")
        assert if_following_lovibot is True

        # if_following() throws an exception if the user doesn't exist
        with pytest.raises(UserNotFound, match="User 'IDontExists' not found."):
            User.if_following(gitea, "IDontExists")


def test_get_repos():
    with Gitea(url=pytest.url, token=pytest.token, log_level="DEBUG") as gitea:
        repos = User.get_repos(gitea, page=1, limit=100)
        for repo in repos:
            assert hasattr(repo, "allow_merge_commits")
            assert type(repo.allow_merge_commits) is bool

            assert hasattr(repo, "allow_rebase")
            assert type(repo.allow_rebase) is bool

            assert hasattr(repo, "allow_rebase_explicit")
            assert type(repo.allow_rebase_explicit) is bool

            assert hasattr(repo, "allow_squash_merge")
            assert type(repo.allow_squash_merge) is bool

            assert hasattr(repo, "archived")
            assert type(repo.archived) is bool

            assert hasattr(repo, "avatar_url")
            assert type(repo.avatar_url) is str

            assert hasattr(repo, "clone_url")
            assert type(repo.clone_url) is str

            assert hasattr(repo, "created_at")
            assert type(repo.created_at) is str

            assert hasattr(repo, "default_branch")
            assert type(repo.default_branch) is str

            assert hasattr(repo, "default_merge_style")
            assert type(repo.default_merge_style) is str

            assert hasattr(repo, "description")
            assert type(repo.description) is str

            assert hasattr(repo, "empty")
            assert type(repo.empty) is bool

            assert hasattr(repo, "fork")
            assert type(repo.fork) is bool

            assert hasattr(repo, "forks_count")
            assert type(repo.forks_count) is int

            assert hasattr(repo, "full_name")
            assert type(repo.full_name) is str

            assert hasattr(repo, "has_issues")
            assert type(repo.has_issues) is bool

            assert hasattr(repo, "has_projects")
            assert type(repo.has_projects) is bool

            assert hasattr(repo, "has_pull_requests")
            assert type(repo.has_pull_requests) is bool

            assert hasattr(repo, "has_wiki")
            assert type(repo.has_wiki) is bool

            assert hasattr(repo, "html_url")
            assert type(repo.html_url) is str

            assert hasattr(repo, "id")
            assert type(repo.id) is int

            assert hasattr(repo, "ignore_whitespace_conflicts")
            assert type(repo.ignore_whitespace_conflicts) is bool

            assert hasattr(repo, "internal")
            assert type(repo.internal) is bool

            assert hasattr(repo, "language")
            assert type(repo.language) is str

            assert hasattr(repo, "languages_url")
            assert type(repo.languages_url) is str

            assert hasattr(repo, "mirror")
            assert type(repo.mirror) is bool

            assert hasattr(repo, "mirror_interval")
            assert type(repo.mirror_interval) is str

            assert hasattr(repo, "mirror_updated")
            assert type(repo.mirror_updated) is str

            assert hasattr(repo, "name")
            assert type(repo.name) is str

            assert hasattr(repo, "open_issues_count")
            assert type(repo.open_issues_count) is int

            assert hasattr(repo, "open_pr_counter")
            assert type(repo.open_pr_counter) is int

            assert hasattr(repo, "original_url")
            assert type(repo.original_url) is str

            assert hasattr(repo, "owner")
            assert type(repo.owner) is dict  # TODO: check type

            assert hasattr(repo, "parent")  # TODO: check type

            assert hasattr(repo, "permissions")
            assert type(repo.permissions) is dict  # TODO: check type

            assert hasattr(repo, "size")
            assert type(repo.size) is int

            assert hasattr(repo, "ssh_url")
            assert type(repo.ssh_url) is str

            assert hasattr(repo, "stars_count")
            assert type(repo.stars_count) is int

            assert hasattr(repo, "template")
            assert type(repo.template) is bool

            assert hasattr(repo, "updated_at")
            assert type(repo.updated_at) is str

            assert hasattr(repo, "watchers_count")
            assert type(repo.watchers_count) is int

            assert hasattr(repo, "website")
            assert type(repo.website) is str


def test_get_settings():
    with Gitea(url=pytest.url, token=pytest.token, log_level="DEBUG") as gitea:
        settings = User.get_settings(gitea)

        assert hasattr(settings, "description")
        assert type(settings.description) is str

        assert hasattr(settings, "diff_view_style")
        assert type(settings.diff_view_style) is str

        assert hasattr(settings, "full_name")
        assert type(settings.full_name) is str

        assert hasattr(settings, "hide_activity")
        assert type(settings.hide_activity) is bool

        assert hasattr(settings, "hide_email")
        assert type(settings.hide_email) is bool

        assert hasattr(settings, "language")
        assert type(settings.language) is str

        assert hasattr(settings, "location")
        assert type(settings.location) is str

        assert hasattr(settings, "theme")
        assert type(settings.theme) is str

        assert hasattr(settings, "website")
        assert type(settings.website) is str
