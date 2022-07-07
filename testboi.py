import os
from giteapy.gitea import Gitea
from giteapy.user import User
from dotenv import load_dotenv


load_dotenv()
GITEA_URL: str = os.environ["GITEA_URL"]
GITEA_TOKEN: str = os.environ["GITEA_TOKEN"]

with Gitea(GITEA_URL, GITEA_TOKEN, log_level="DEBUG") as gitea:
    user = User.get_user(gitea)

    assert hasattr(user, "active")
    assert type(user.active) is bool
    print(f"user.active = {user.active}")

    assert hasattr(user, "avatar_url")
    assert type(user.avatar_url) is str
    print(f"user.avatar_url = {user.avatar_url}")

    assert hasattr(user, "created")
    assert type(user.created) is str
    print(f"user.created = {user.created}")

    assert hasattr(user, "description")
    assert type(user.description) is str
    print(f"user.description = {user.description}")

    assert hasattr(user, "email")
    assert type(user.email) is str
    print(f"user.email = {user.email}")

    assert hasattr(user, "followers_count")
    assert type(user.followers_count) is int
    print(f"user.followers_count = {user.followers_count}")

    assert hasattr(user, "following_count")
    assert type(user.following_count) is int
    print(f"user.following_count = {user.following_count}")

    assert hasattr(user, "full_name")
    assert type(user.full_name) is str
    print(f"user.full_name = {user.full_name}")

    assert hasattr(user, "id")
    assert type(user.id) is int
    print(f"user.id = {user.id}")

    assert hasattr(user, "is_admin")
    assert type(user.is_admin) is bool
    print(f"user.is_admin = {user.is_admin}")

    assert hasattr(user, "language")
    assert type(user.language) is str
    print(f"user.language = {user.language}")

    assert hasattr(user, "last_login")
    assert type(user.last_login) is str
    print(f"user.last_login = {user.last_login}")

    assert hasattr(user, "location")
    assert type(user.location) is str
    print(f"user.location = {user.location}")

    assert hasattr(user, "login")
    assert type(user.login) is str
    print(f"user.login = {user.login}")

    assert hasattr(user, "prohibit_login")
    assert type(user.prohibit_login) is bool
    print(f"user.prohibit_login = {user.prohibit_login}")

    assert hasattr(user, "restricted")
    assert type(user.restricted) is bool
    print(f"user.restricted = {user.restricted}")

    assert hasattr(user, "starred_repos_count")
    assert type(user.starred_repos_count) is int
    print(f"user.starred_repos_count = {user.starred_repos_count}")

    assert hasattr(user, "visibility")
    assert type(user.visibility) is str
    print(f"user.visibility = {user.visibility}")

    assert hasattr(user, "website")
    assert type(user.website) is str
    print(f"user.website = {user.website}")

    print("\n\n")
    followers = User.get_followers(gitea, page=1, limit=10)
    for follower in followers:
        assert hasattr(follower, "active")
        assert type(follower.active) is bool
        print(f"follower.active = {follower.active}")

        assert hasattr(follower, "avatar_url")
        assert type(follower.avatar_url) is str
        print(f"follower.avatar_url = {follower.avatar_url}")

        assert hasattr(follower, "created")
        assert type(follower.created) is str
        print(f"follower.created = {follower.created}")

        assert hasattr(follower, "description")
        assert type(follower.description) is str
        print(f"follower.description = {follower.description}")

        assert hasattr(follower, "email")
        assert type(follower.email) is str
        print(f"follower.email = {follower.email}")

        assert hasattr(follower, "followers_count")
        assert type(follower.followers_count) is int
        print(f"follower.followers_count = {follower.followers_count}")

        assert hasattr(follower, "following_count")
        assert type(follower.following_count) is int
        print(f"follower.following_count = {follower.following_count}")

        assert hasattr(follower, "full_name")
        assert type(follower.full_name) is str
        print(f"follower.full_name = {follower.full_name}")

        assert hasattr(follower, "id")
        assert type(follower.id) is int
        print(f"follower.id = {follower.id}")

        assert hasattr(follower, "is_admin")
        assert type(follower.is_admin) is bool
        print(f"follower.is_admin = {follower.is_admin}")

        assert hasattr(follower, "language")
        assert type(follower.language) is str
        print(f"follower.language = {follower.language}")

        assert hasattr(follower, "last_login")
        assert type(follower.last_login) is str
        print(f"follower.last_login = {follower.last_login}")

        assert hasattr(follower, "location")
        assert type(follower.location) is str
        print(f"follower.location = {follower.location}")

        assert hasattr(follower, "login")
        assert type(follower.login) is str
        print(f"follower.login = {follower.login}")

        assert hasattr(follower, "prohibit_login")
        assert type(follower.prohibit_login) is bool
        print(f"follower.prohibit_login = {follower.prohibit_login}")

        assert hasattr(follower, "restricted")
        assert type(follower.restricted) is bool
        print(f"follower.restricted = {follower.restricted}")

        assert hasattr(follower, "starred_repos_count")
        assert type(follower.starred_repos_count) is int
        print(f"follower.starred_repos_count = {follower.starred_repos_count}")

        assert hasattr(follower, "visibility")
        assert type(follower.visibility) is str
        print(f"follower.visibility = {follower.visibility}")

        assert hasattr(follower, "website")
        assert type(follower.website) is str
        print(f"follower.website = {follower.website}")

    print("\n\n")
    following = User.get_following(gitea, page=1, limit=10)
    for follow in following:
        assert hasattr(follow, "active")
        assert type(follow.active) is bool
        print(f"follow.active = {follow.active}")

        assert hasattr(follow, "avatar_url")
        assert type(follow.avatar_url) is str
        print(f"follow.avatar_url = {follow.avatar_url}")

        assert hasattr(follow, "created")
        assert type(follow.created) is str
        print(f"follow.created = {follow.created}")

        assert hasattr(follow, "description")
        assert type(follow.description) is str
        print(f"follow.description = {follow.description}")

        assert hasattr(follow, "email")
        assert type(follow.email) is str
        print(f"follow.email = {follow.email}")

        assert hasattr(follow, "followers_count")
        assert type(follow.followers_count) is int
        print(f"follow.follows_count = {follow.followers_count}")

        assert hasattr(follow, "following_count")
        assert type(follow.following_count) is int
        print(f"follow.following_count = {follow.following_count}")

        assert hasattr(follow, "full_name")
        assert type(follow.full_name) is str
        print(f"follow.full_name = {follow.full_name}")

        assert hasattr(follow, "id")
        assert type(follow.id) is int
        print(f"follow.id = {follow.id}")

        assert hasattr(follow, "is_admin")
        assert type(follow.is_admin) is bool
        print(f"follow.is_admin = {follow.is_admin}")

        assert hasattr(follow, "language")
        assert type(follow.language) is str
        print(f"follow.language = {follow.language}")

        assert hasattr(follow, "last_login")
        assert type(follow.last_login) is str
        print(f"follow.last_login = {follow.last_login}")

        assert hasattr(follow, "location")
        assert type(follow.location) is str
        print(f"follow.location = {follow.location}")

        assert hasattr(follow, "login")
        assert type(follow.login) is str
        print(f"follow.login = {follow.login}")

        assert hasattr(follow, "prohibit_login")
        assert type(follow.prohibit_login) is bool
        print(f"follow.prohibit_login = {follow.prohibit_login}")

        assert hasattr(follow, "restricted")
        assert type(follow.restricted) is bool
        print(f"follow.restricted = {follow.restricted}")

        assert hasattr(follow, "starred_repos_count")
        assert type(follow.starred_repos_count) is int
        print(f"follow.starred_repos_count = {follow.starred_repos_count}")

        assert hasattr(follow, "visibility")
        assert type(follow.visibility) is str
        print(f"follow.visibility = {follow.visibility}")

        assert hasattr(follow, "website")
        assert type(follow.website) is str
        print(f"follow.website = {follow.website}")

    print("\n\n")
    if_following_lovibot = User.if_following(gitea, "LoviBot")
    print(f"if_following LoviBot = {if_following_lovibot}")
    if_following_archive = User.if_following(gitea, "Archive")
    print(f"if_following_false Archive = {if_following_archive}")
