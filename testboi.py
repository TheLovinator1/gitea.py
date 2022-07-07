import os
from giteapy.gitea import Gitea
from giteapy.user import User
from dotenv import load_dotenv
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO)
GITEA_URL: str = os.environ["GITEA_URL"]
GITEA_TOKEN: str = os.environ["GITEA_TOKEN"]


with Gitea(GITEA_URL, GITEA_TOKEN, log_level="DEBUG") as gitea:
    print("\nTesting User.get_user()")
    user = User.get_user(gitea)

    assert hasattr(user, "active")
    assert type(user.active) is bool
    print(f"\tuser.active = {user.active!r}")

    assert hasattr(user, "avatar_url")
    assert type(user.avatar_url) is str
    print(f"\tuser.avatar_url = {user.avatar_url!r}")

    assert hasattr(user, "created")
    assert type(user.created) is str
    print(f"\tuser.created = {user.created!r}")

    assert hasattr(user, "description")
    assert type(user.description) is str
    print(f"\tuser.description = {user.description!r}")

    assert hasattr(user, "email")
    assert type(user.email) is str
    print(f"\tuser.email = {user.email!r}")

    assert hasattr(user, "followers_count")
    assert type(user.followers_count) is int
    print(f"\tuser.followers_count = {user.followers_count!r}")

    assert hasattr(user, "following_count")
    assert type(user.following_count) is int
    print(f"\tuser.following_count = {user.following_count!r}")

    assert hasattr(user, "full_name")
    assert type(user.full_name) is str
    print(f"\tuser.full_name = {user.full_name!r}")

    assert hasattr(user, "id")
    assert type(user.id) is int
    print(f"\tuser.id = {user.id!r}")

    assert hasattr(user, "is_admin")
    assert type(user.is_admin) is bool
    print(f"\tuser.is_admin = {user.is_admin!r}")

    assert hasattr(user, "language")
    assert type(user.language) is str
    print(f"\tuser.language = {user.language!r}")

    assert hasattr(user, "last_login")
    assert type(user.last_login) is str
    print(f"\tuser.last_login = {user.last_login!r}")

    assert hasattr(user, "location")
    assert type(user.location) is str
    print(f"\tuser.location = {user.location!r}")

    assert hasattr(user, "login")
    assert type(user.login) is str
    print(f"\tuser.login = {user.login!r}")

    assert hasattr(user, "prohibit_login")
    assert type(user.prohibit_login) is bool
    print(f"\tuser.prohibit_login = {user.prohibit_login!r}")

    assert hasattr(user, "restricted")
    assert type(user.restricted) is bool
    print(f"\tuser.restricted = {user.restricted!r}")

    assert hasattr(user, "starred_repos_count")
    assert type(user.starred_repos_count) is int
    print(f"\tuser.starred_repos_count = {user.starred_repos_count!r}")

    assert hasattr(user, "visibility")
    assert type(user.visibility) is str
    print(f"\tuser.visibility = {user.visibility!r}")

    assert hasattr(user, "website")
    assert type(user.website) is str
    print(f"\tuser.website = {user.website!r}")

    print("\nTesting User.get_followers()")
    followers = User.get_followers(gitea, page=1, limit=10)
    for follower in followers:
        assert hasattr(follower, "active")
        assert type(follower.active) is bool
        print(f"\tfollower.active = {follower.active!r}")

        assert hasattr(follower, "avatar_url")
        assert type(follower.avatar_url) is str
        print(f"\tfollower.avatar_url = {follower.avatar_url!r}")

        assert hasattr(follower, "created")
        assert type(follower.created) is str
        print(f"\tfollower.created = {follower.created!r}")

        assert hasattr(follower, "description")
        assert type(follower.description) is str
        print(f"\tfollower.description = {follower.description!r}")

        assert hasattr(follower, "email")
        assert type(follower.email) is str
        print(f"\tfollower.email = {follower.email!r}")

        assert hasattr(follower, "followers_count")
        assert type(follower.followers_count) is int
        print(f"\tfollower.followers_count = {follower.followers_count!r}")

        assert hasattr(follower, "following_count")
        assert type(follower.following_count) is int
        print(f"\tfollower.following_count = {follower.following_count!r}")

        assert hasattr(follower, "full_name")
        assert type(follower.full_name) is str
        print(f"\tfollower.full_name = {follower.full_name!r}")

        assert hasattr(follower, "id")
        assert type(follower.id) is int
        print(f"\tfollower.id = {follower.id!r}")

        assert hasattr(follower, "is_admin")
        assert type(follower.is_admin) is bool
        print(f"\tfollower.is_admin = {follower.is_admin!r}")

        assert hasattr(follower, "language")
        assert type(follower.language) is str
        print(f"\tfollower.language = {follower.language!r}")

        assert hasattr(follower, "last_login")
        assert type(follower.last_login) is str
        print(f"\tfollower.last_login = {follower.last_login!r}")

        assert hasattr(follower, "location")
        assert type(follower.location) is str
        print(f"\tfollower.location = {follower.location!r}")

        assert hasattr(follower, "login")
        assert type(follower.login) is str
        print(f"\tfollower.login = {follower.login!r}")

        assert hasattr(follower, "prohibit_login")
        assert type(follower.prohibit_login) is bool
        print(f"\tfollower.prohibit_login = {follower.prohibit_login!r}")

        assert hasattr(follower, "restricted")
        assert type(follower.restricted) is bool
        print(f"\tfollower.restricted = {follower.restricted!r}")

        assert hasattr(follower, "starred_repos_count")
        assert type(follower.starred_repos_count) is int
        print(f"\tfollower.starred_repos_count = {follower.starred_repos_count!r}")

        assert hasattr(follower, "visibility")
        assert type(follower.visibility) is str
        print(f"\tfollower.visibility = {follower.visibility!r}")

        assert hasattr(follower, "website")
        assert type(follower.website) is str
        print(f"\tfollower.website = {follower.website!r}")

    print("\nTesting User.get_following()")
    following = User.get_following(gitea, page=1, limit=10)
    for follow in following:
        assert hasattr(follow, "active")
        assert type(follow.active) is bool
        print(f"\tfollow.active = {follow.active!r}")

        assert hasattr(follow, "avatar_url")
        assert type(follow.avatar_url) is str
        print(f"\tfollow.avatar_url = {follow.avatar_url!r}")

        assert hasattr(follow, "created")
        assert type(follow.created) is str
        print(f"\tfollow.created = {follow.created!r}")

        assert hasattr(follow, "description")
        assert type(follow.description) is str
        print(f"\tfollow.description = {follow.description!r}")

        assert hasattr(follow, "email")
        assert type(follow.email) is str
        print(f"\tfollow.email = {follow.email!r}")

        assert hasattr(follow, "followers_count")
        assert type(follow.followers_count) is int
        print(f"\tfollow.follows_count = {follow.followers_count!r}")

        assert hasattr(follow, "following_count")
        assert type(follow.following_count) is int
        print(f"\tfollow.following_count = {follow.following_count!r}")

        assert hasattr(follow, "full_name")
        assert type(follow.full_name) is str
        print(f"\tfollow.full_name = {follow.full_name!r}")

        assert hasattr(follow, "id")
        assert type(follow.id) is int
        print(f"\tfollow.id = {follow.id!r}")

        assert hasattr(follow, "is_admin")
        assert type(follow.is_admin) is bool
        print(f"\tfollow.is_admin = {follow.is_admin!r}")

        assert hasattr(follow, "language")
        assert type(follow.language) is str
        print(f"\tfollow.language = {follow.language!r}")

        assert hasattr(follow, "last_login")
        assert type(follow.last_login) is str
        print(f"\tfollow.last_login = {follow.last_login!r}")

        assert hasattr(follow, "location")
        assert type(follow.location) is str
        print(f"\tfollow.location = {follow.location!r}")

        assert hasattr(follow, "login")
        assert type(follow.login) is str
        print(f"\tfollow.login = {follow.login!r}")

        assert hasattr(follow, "prohibit_login")
        assert type(follow.prohibit_login) is bool
        print(f"\tfollow.prohibit_login = {follow.prohibit_login!r}")

        assert hasattr(follow, "restricted")
        assert type(follow.restricted) is bool
        print(f"\tfollow.restricted = {follow.restricted!r}")

        assert hasattr(follow, "starred_repos_count")
        assert type(follow.starred_repos_count) is int
        print(f"\tfollow.starred_repos_count = {follow.starred_repos_count!r}")

        assert hasattr(follow, "visibility")
        assert type(follow.visibility) is str
        print(f"\tfollow.visibility = {follow.visibility!r}")

        assert hasattr(follow, "website")
        assert type(follow.website) is str
        print(f"\tfollow.website = {follow.website!r}")

    print("\nTesting if_following():")
    if_following_lovibot = User.if_following(gitea, "LoviBot")
    print(f"\tif_following LoviBot = {if_following_lovibot!r}")
    assert if_following_lovibot is True

    if_following_archive = User.if_following(gitea, "Archive")
    print(f"\tif_following Archive = {if_following_archive!r}")
    assert if_following_archive is False
