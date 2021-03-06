import os
from giteapy.gitea import Gitea
from giteapy.user import User
from giteapy.admin import Admin
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

    assert hasattr(user, "created_at")
    assert type(user.created_at) is str
    print(f"\tuser.created_at = {user.created_at!r}")

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

        assert hasattr(follower, "created_at")
        assert type(follower.created_at) is str
        print(f"\tfollower.created_at = {follower.created_at!r}")

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

        assert hasattr(follow, "created_at")
        assert type(follow.created_at) is str
        print(f"\tfollow.created_at = {follow.created_at!r}")

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

    print("\nTesting User.get_repos()")
    repos = User.get_repos(gitea, page=1, limit=100)
    for repo in repos:
        assert hasattr(repo, "allow_merge_commits")
        assert type(repo.allow_merge_commits) is bool
        print(f"\trepo.allow_merge_commits = {repo.allow_merge_commits!r}")

        assert hasattr(repo, "allow_rebase")
        assert type(repo.allow_rebase) is bool
        print(f"\trepo.allow_rebase = {repo.allow_rebase!r}")

        assert hasattr(repo, "allow_rebase_explicit")
        assert type(repo.allow_rebase_explicit) is bool
        print(f"\trepo.allow_rebase_explicit = {repo.allow_rebase_explicit!r}")

        assert hasattr(repo, "allow_squash_merge")
        assert type(repo.allow_squash_merge) is bool
        print(f"\trepo.allow_squash_merge = {repo.allow_squash_merge!r}")

        assert hasattr(repo, "archived")
        assert type(repo.archived) is bool
        print(f"\trepo.archived = {repo.archived!r}")

        assert hasattr(repo, "avatar_url")
        assert type(repo.avatar_url) is str
        print(f"\trepo.avatar_url = {repo.avatar_url!r}")

        assert hasattr(repo, "clone_url")
        assert type(repo.clone_url) is str
        print(f"\trepo.clone_url = {repo.clone_url!r}")

        assert hasattr(repo, "created_at")
        assert type(repo.created_at) is str
        print(f"\trepo.created_at = {repo.created_at!r}")

        assert hasattr(repo, "default_branch")
        assert type(repo.default_branch) is str
        print(f"\trepo.default_branch = {repo.default_branch!r}")

        assert hasattr(repo, "default_merge_style")
        assert type(repo.default_merge_style) is str
        print(f"\trepo.default_merge_style = {repo.default_merge_style!r}")

        assert hasattr(repo, "description")
        assert type(repo.description) is str
        print(f"\trepo.description = {repo.description!r}")

        assert hasattr(repo, "empty")
        assert type(repo.empty) is bool
        print(f"\trepo.empty = {repo.empty!r}")

        assert hasattr(repo, "fork")
        assert type(repo.fork) is bool
        print(f"\trepo.fork = {repo.fork!r}")

        assert hasattr(repo, "forks_count")
        assert type(repo.forks_count) is int
        print(f"\trepo.forks_count = {repo.forks_count!r}")

        assert hasattr(repo, "full_name")
        assert type(repo.full_name) is str
        print(f"\trepo.full_name = {repo.full_name!r}")

        assert hasattr(repo, "has_issues")
        assert type(repo.has_issues) is bool
        print(f"\trepo.has_issues = {repo.has_issues!r}")

        assert hasattr(repo, "has_projects")
        assert type(repo.has_projects) is bool
        print(f"\trepo.has_projects = {repo.has_projects!r}")

        assert hasattr(repo, "has_pull_requests")
        assert type(repo.has_pull_requests) is bool
        print(f"\trepo.has_pull_requests = {repo.has_pull_requests!r}")

        assert hasattr(repo, "has_wiki")
        assert type(repo.has_wiki) is bool
        print(f"\trepo.has_wiki = {repo.has_wiki!r}")

        assert hasattr(repo, "html_url")
        assert type(repo.html_url) is str
        print(f"\trepo.html_url = {repo.html_url!r}")

        assert hasattr(repo, "id")
        assert type(repo.id) is int
        print(f"\trepo.id = {repo.id!r}")

        assert hasattr(repo, "ignore_whitespace_conflicts")
        assert type(repo.ignore_whitespace_conflicts) is bool
        print(f"\trepo.ignore_whitespace_conflicts = {repo.ignore_whitespace_conflicts!r}")

        assert hasattr(repo, "internal")
        assert type(repo.internal) is bool
        print(f"\trepo.internal = {repo.internal!r}")

        assert hasattr(repo, "language")
        assert type(repo.language) is str
        print(f"\trepo.language = {repo.language!r}")

        assert hasattr(repo, "languages_url")
        assert type(repo.languages_url) is str
        print(f"\trepo.languages_url = {repo.languages_url!r}")

        assert hasattr(repo, "mirror")
        assert type(repo.mirror) is bool
        print(f"\trepo.mirror = {repo.mirror!r}")

        assert hasattr(repo, "mirror_interval")
        assert type(repo.mirror_interval) is str
        print(f"\trepo.mirror_interval = {repo.mirror_interval!r}")

        assert hasattr(repo, "mirror_updated")
        assert type(repo.mirror_updated) is str
        print(f"\trepo.mirror_updated = {repo.mirror_updated!r}")

        assert hasattr(repo, "name")
        assert type(repo.name) is str
        print(f"\trepo.name = {repo.name!r}")

        assert hasattr(repo, "open_issues_count")
        assert type(repo.open_issues_count) is int
        print(f"\trepo.open_issues_count = {repo.open_issues_count!r}")

        assert hasattr(repo, "open_pr_counter")
        assert type(repo.open_pr_counter) is int
        print(f"\trepo.open_pr_counter = {repo.open_pr_counter!r}")

        assert hasattr(repo, "original_url")
        assert type(repo.original_url) is str
        print(f"\trepo.original_url = {repo.original_url!r}")

        assert hasattr(repo, "owner")
        assert type(repo.owner) is dict  # TODO: check type
        print(f"\trepo.owner = {repo.owner!r}")

        assert hasattr(repo, "parent")
        print(f"\trepo.parent = {repo.parent!r}")

        assert hasattr(repo, "permissions")
        assert type(repo.permissions) is dict  # TODO: check type
        print(f"\trepo.permissions = {repo.permissions!r}")

        assert hasattr(repo, "size")
        assert type(repo.size) is int
        print(f"\trepo.size = {repo.size!r}")

        assert hasattr(repo, "ssh_url")
        assert type(repo.ssh_url) is str
        print(f"\trepo.ssh_url = {repo.ssh_url!r}")

        assert hasattr(repo, "stars_count")
        assert type(repo.stars_count) is int
        print(f"\trepo.stars_count = {repo.stars_count!r}")

        assert hasattr(repo, "template")
        assert type(repo.template) is bool
        print(f"\trepo.template = {repo.template!r}")

        assert hasattr(repo, "updated_at")
        assert type(repo.updated_at) is str
        print(f"\trepo.updated_at = {repo.updated_at!r}")

        assert hasattr(repo, "watchers_count")
        assert type(repo.watchers_count) is int
        print(f"\trepo.watchers_count = {repo.watchers_count!r}")

        assert hasattr(repo, "website")
        assert type(repo.website) is str
        print(f"\trepo.website = {repo.website!r}")

    print("\nTesting User.get_settings()")
    settings = User.get_settings(gitea)
    assert hasattr(settings, "description")
    assert type(settings.description) is str
    print(f"\tsettings.description = {settings.description!r}")

    assert hasattr(settings, "diff_view_style")
    assert type(settings.diff_view_style) is str
    print(f"\tsettings.diff_view_style = {settings.diff_view_style!r}")

    assert hasattr(settings, "full_name")
    assert type(settings.full_name) is str
    print(f"\tsettings.full_name = {settings.full_name!r}")

    assert hasattr(settings, "hide_activity")
    assert type(settings.hide_activity) is bool
    print(f"\tsettings.hide_activity = {settings.hide_activity!r}")

    assert hasattr(settings, "hide_email")
    assert type(settings.hide_email) is bool
    print(f"\tsettings.hide_email = {settings.hide_email!r}")

    assert hasattr(settings, "language")
    assert type(settings.language) is str
    print(f"\tsettings.language = {settings.language!r}")

    assert hasattr(settings, "location")
    assert type(settings.location) is str
    print(f"\tsettings.location = {settings.location!r}")

    assert hasattr(settings, "theme")
    assert type(settings.theme) is str
    print(f"\tsettings.theme = {settings.theme!r}")

    assert hasattr(settings, "website")
    assert type(settings.website) is str
    print(f"\tsettings.website = {settings.website!r}")

    print("\nTesting User.get_starred()")
    starred = User.get_starred(gitea, page=1, limit=100)
    for star in starred:
        assert hasattr(star, "allow_merge_commits")
        assert type(star.allow_merge_commits) is bool
        print(f"\tstar.allow_merge_commits = {star.allow_merge_commits!r}")

        assert hasattr(star, "allow_rebase")
        assert type(star.allow_rebase) is bool
        print(f"\tstar.allow_rebase = {star.allow_rebase!r}")

        assert hasattr(star, "allow_rebase_explicit")
        assert type(star.allow_rebase_explicit) is bool
        print(f"\tstar.allow_rebase_explicit = {star.allow_rebase_explicit!r}")

        assert hasattr(star, "allow_squash_merge")
        assert type(star.allow_squash_merge) is bool
        print(f"\tstar.allow_squash_merge = {star.allow_squash_merge!r}")

        assert hasattr(star, "archived")
        assert type(star.archived) is bool
        print(f"\tstar.archived = {star.archived!r}")

        assert hasattr(star, "avatar_url")
        assert type(star.avatar_url) is str
        print(f"\tstar.avatar_url = {star.avatar_url!r}")

        assert hasattr(star, "clone_url")
        assert type(star.clone_url) is str
        print(f"\tstar.clone_url = {star.clone_url!r}")

        assert hasattr(star, "created_at")
        assert type(star.created_at) is str
        print(f"\tstar.created_at = {star.created_at!r}")

        assert hasattr(star, "default_branch")
        assert type(star.default_branch) is str
        print(f"\tstar.default_branch = {star.default_branch!r}")

        assert hasattr(star, "default_merge_style")
        assert type(star.default_merge_style) is str
        print(f"\tstar.default_merge_style = {star.default_merge_style!r}")

        assert hasattr(star, "description")
        assert type(star.description) is str
        print(f"\tstar.description = {star.description!r}")

        assert hasattr(star, "empty")
        assert type(star.empty) is bool
        print(f"\tstar.empty = {star.empty!r}")

        assert hasattr(star, "fork")
        assert type(star.fork) is bool
        print(f"\tstar.fork = {star.fork!r}")

        assert hasattr(star, "forks_count")
        assert type(star.forks_count) is int
        print(f"\tstar.forks_count = {star.forks_count!r}")

        assert hasattr(star, "full_name")
        assert type(star.full_name) is str
        print(f"\tstar.full_name = {star.full_name!r}")

        assert hasattr(star, "has_issues")
        assert type(star.has_issues) is bool
        print(f"\tstar.has_issues = {star.has_issues!r}")

        assert hasattr(star, "has_projects")
        assert type(star.has_projects) is bool
        print(f"\tstar.has_projects = {star.has_projects!r}")

        assert hasattr(star, "has_pull_requests")
        assert type(star.has_pull_requests) is bool
        print(f"\tstar.has_pull_requests = {star.has_pull_requests!r}")

        assert hasattr(star, "has_wiki")
        assert type(star.has_wiki) is bool
        print(f"\tstar.has_wiki = {star.has_wiki!r}")

        assert hasattr(star, "html_url")
        assert type(star.html_url) is str
        print(f"\tstar.html_url = {star.html_url!r}")

        assert hasattr(star, "id")
        assert type(star.id) is int
        print(f"\tstar.id = {star.id!r}")

        assert hasattr(star, "ignore_whitespace_conflicts")
        assert type(star.ignore_whitespace_conflicts) is bool
        print(f"\tstar.ignore_whitespace_conflicts = {star.ignore_whitespace_conflicts!r}")

        assert hasattr(star, "internal")
        assert type(star.internal) is bool
        print(f"\tstar.internal = {star.internal!r}")

        assert hasattr(star, "language")
        assert type(star.language) is str
        print(f"\tstar.language = {star.language!r}")

        assert hasattr(star, "languages_url")
        assert type(star.languages_url) is str
        print(f"\tstar.languages_url = {star.languages_url!r}")

        assert hasattr(star, "mirror")
        assert type(star.mirror) is bool
        print(f"\tstar.mirror = {star.mirror!r}")

        assert hasattr(star, "mirror_interval")
        assert type(star.mirror_interval) is str
        print(f"\tstar.mirror_interval = {star.mirror_interval!r}")

        assert hasattr(star, "mirror_updated")
        assert type(star.mirror_updated) is str
        print(f"\tstar.mirror_updated = {star.mirror_updated!r}")

        assert hasattr(star, "name")
        assert type(star.name) is str
        print(f"\tstar.name = {star.name!r}")

        assert hasattr(star, "open_issues_count")
        assert type(star.open_issues_count) is int
        print(f"\tstar.open_issues_count = {star.open_issues_count!r}")

        assert hasattr(star, "open_pr_counter")
        assert type(star.open_pr_counter) is int
        print(f"\tstar.open_pr_counter = {star.open_pr_counter!r}")

        assert hasattr(star, "original_url")
        assert type(star.original_url) is str
        print(f"\tstar.original_url = {star.original_url!r}")

        assert hasattr(star, "owner")
        assert type(star.owner) is dict  # TODO: check type
        print(f"\tstar.owner = {star.owner!r}")

        assert hasattr(star, "parent")
        print(f"\tstar.parent = {star.parent!r}")

        assert hasattr(star, "permissions")
        assert type(star.permissions) is dict  # TODO: check type
        print(f"\tstar.permissions = {star.permissions!r}")

        assert hasattr(star, "size")
        assert type(star.size) is int
        print(f"\tstar.size = {star.size!r}")

        assert hasattr(star, "ssh_url")
        assert type(star.ssh_url) is str
        print(f"\tstar.ssh_url = {star.ssh_url!r}")

        assert hasattr(star, "stars_count")
        assert type(star.stars_count) is int
        print(f"\tstar.stars_count = {star.stars_count!r}")

        assert hasattr(star, "template")
        assert type(star.template) is bool
        print(f"\tstar.template = {star.template!r}")

        assert hasattr(star, "updated_at")
        assert type(star.updated_at) is str
        print(f"\tstar.updated_at = {star.updated_at!r}")

        assert hasattr(star, "watchers_count")
        assert type(star.watchers_count) is int
        print(f"\tstar.watchers_count = {star.watchers_count!r}")

        assert hasattr(star, "website")
        assert type(star.website) is str
        print(f"\tstar.website = {star.website!r}")

    print("\nTesting User.get_oauth2_applications()")
    oauth2_apps = User.get_oauth2_applications(gitea, page=1, limit=100)
    for app in oauth2_apps:
        assert hasattr(app, "client_id")
        assert type(app.client_id) is str
        print(f"\tapp.client_id = {app.client_id!r}")

        assert hasattr(app, "client_secret")
        assert type(app.client_secret) is str
        print(f"\tapp.client_secret = {app.client_secret!r}")

        assert hasattr(app, "created_at")
        assert type(app.created_at) is str
        print(f"\tapp.created_at = {app.created_at!r}")

        assert hasattr(app, "id")
        assert type(app.id) is int
        print(f"\tapp.id = {app.id!r}")
        oauth2_id = app.id  # For get_oauth2_application_by_id()

        assert hasattr(app, "name")
        assert type(app.name) is str
        print(f"\tapp.name = {app.name!r}")

        assert hasattr(app, "redirect_uris")
        assert type(app.redirect_uris) is list
        print(f"\tapp.redirect_uris = {app.redirect_uris!r}")
        for uri in app.redirect_uris:
            print(f"\t\turi = {uri!r}")

    print("\nTesting User.get_oauth2_application_by_id()")
    oauth2 = User.get_oauth2_application_by_id(gitea, id=oauth2_id)
    assert hasattr(oauth2, "client_id")
    assert type(oauth2.client_id) is str
    print(f"\toauth2.client_id = {oauth2.client_id!r}")

    assert hasattr(oauth2, "client_secret")
    assert type(oauth2.client_secret) is str
    print(f"\toauth2.client_secret = {oauth2.client_secret!r}")

    assert hasattr(oauth2, "created_at")
    assert type(oauth2.created_at) is str
    print(f"\toauth2.created_at = {oauth2.created_at!r}")

    assert hasattr(oauth2, "id")
    assert type(oauth2.id) is int
    print(f"\toauth2.id = {oauth2.id!r}")

    assert hasattr(oauth2, "name")
    assert type(oauth2.name) is str
    print(f"\toauth2.name = {oauth2.name!r}")

    assert hasattr(oauth2, "redirect_uris")
    assert type(oauth2.redirect_uris) is list
    print(f"\toauth2.redirect_uris = {oauth2.redirect_uris!r}")

    for uri in oauth2.redirect_uris:
        print(f"\t\turi = {uri!r}")

    gpg_key_token = User.get_gpg_key_token(gitea)
    print(f"\npgp_key_token = {gpg_key_token!r}")
    assert type(gpg_key_token) is str

    gpg_keys = User.get_gpg_keys(gitea, page=1, limit=100)
    for key in gpg_keys:
        assert hasattr(key, "can_certify")
        assert type(key.can_certify) is bool
        print(f"\tkey.can_certify = {key.can_certify!r}")

        assert hasattr(key, "can_encrypt_comms")
        assert type(key.can_encrypt_comms) is bool
        print(f"\tkey.can_encrypt_comms = {key.can_encrypt_comms!r}")

        assert hasattr(key, "can_encrypt_storage")
        assert type(key.can_encrypt_storage) is bool
        print(f"\tkey.can_encrypt_storage = {key.can_encrypt_storage!r}")

        assert hasattr(key, "can_sign")
        assert type(key.can_sign) is bool
        print(f"\tkey.can_sign = {key.can_sign!r}")

        assert hasattr(key, "created_at")
        assert type(key.created_at) is str
        print(f"\tkey.created_at = {key.created_at!r}")

        assert hasattr(key, "emails")
        assert type(key.emails) is list
        for email in key.emails:
            print(f"\t\temail = {email!r}")

        assert hasattr(key, "expires_at")
        assert type(key.expires_at) is str
        print(f"\tkey.expires_at = {key.expires_at!r}")

        assert hasattr(key, "id")
        assert type(key.id) is int
        print(f"\tkey.id = {key.id!r}")
        gpg_key_id = key.id  # For get_gpg_key_by_id()

        assert hasattr(key, "key_id")
        assert type(key.key_id) is str
        print(f"\tkey.key_id = {key.key_id!r}")

        assert hasattr(key, "primary_key_id")
        assert type(key.primary_key_id) is str
        print(f"\tkey.primary_key_id = {key.primary_key_id!r}")

        assert hasattr(key, "public_key")
        assert type(key.public_key) is str
        print(f"\tkey.public_key = {key.public_key!r}")

        assert hasattr(key, "subkeys")
        assert type(key.subkeys) is list
        for subkey in key.subkeys:
            print(f"\t\tsubkey = {subkey!r}")

        assert hasattr(key, "verified")
        assert type(key.verified) is bool
        print(f"\tkey.verified = {key.verified!r}")

    print("\nTesting User.get_gpg_key_by_id()")
    gpg_key = User.get_gpg_key_by_id(gitea, id=gpg_key_id)
    assert hasattr(gpg_key, "can_certify")
    assert type(gpg_key.can_certify) is bool
    print(f"\tgpg_key.can_certify = {gpg_key.can_certify!r}")

    assert hasattr(gpg_key, "can_encrypt_comms")
    assert type(gpg_key.can_encrypt_comms) is bool
    print(f"\tgpg_key.can_encrypt_comms = {gpg_key.can_encrypt_comms!r}")

    assert hasattr(gpg_key, "can_encrypt_storage")
    assert type(gpg_key.can_encrypt_storage) is bool
    print(f"\tgpg_key.can_encrypt_storage = {gpg_key.can_encrypt_storage!r}")

    assert hasattr(gpg_key, "can_sign")
    assert type(gpg_key.can_sign) is bool
    print(f"\tgpg_key.can_sign = {gpg_key.can_sign!r}")

    assert hasattr(gpg_key, "created_at")
    assert type(gpg_key.created_at) is str
    print(f"\tgpg_key.created_at = {gpg_key.created_at!r}")

    assert hasattr(gpg_key, "emails")
    assert type(gpg_key.emails) is list
    for email in gpg_key.emails:
        print(f"\t\temail = {email!r}")

    assert hasattr(gpg_key, "expires_at")
    assert type(gpg_key.expires_at) is str
    print(f"\tgpg_key.expires_at = {gpg_key.expires_at!r}")

    assert hasattr(gpg_key, "id")
    assert type(gpg_key.id) is int
    print(f"\tgpg_key.id = {gpg_key.id!r}")

    tasks = Admin.cron_tasks(gitea, page=1, limit=100)
    for task in tasks:
        assert hasattr(task, "exec_times")
        assert type(task.exec_times) is int

        assert hasattr(task, "name")
        assert type(task.name) is str

        assert hasattr(task, "next")
        assert type(task.next) is str

        assert hasattr(task, "prev")
        assert type(task.prev) is str

        assert hasattr(task, "schedule")
        assert type(task.schedule) is str
        print(f"\ttask: {task.name!r}")

    print("Done :-)")
