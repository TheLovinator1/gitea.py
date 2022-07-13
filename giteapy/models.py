from dataclasses import dataclass
from typing import List


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
    # TODO: created_at and last_login is a string, but it should be a datetime ("created": "2022-07-06T14:33:25.419Z")
    """

    created_at: str
    time: int
    user_name: str


@dataclass
class UserModel:
    """User represents a user on Gitea.

    Attributes:
        active: Is the user active?
        avatar_url: URL to the user's avatar.
        created_at: When the user was created.
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

    # TODO: created_at and last_login is a string, but it should be a datetime ("created": "2022-07-06T14:33:25.419Z")
    """

    active: bool
    avatar_url: str
    created_at: str
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


@dataclass
class ExternalTrackerModel:
    """ExternalTrackerModel represents an external tracker.

    external_tracker_format: External Issue Tracker URL Format. Use the
        placeholders {user}, {repo} and {index} for the username, repository name
        and issue index.
    external_tracker_style: External Issue Tracker Number Format, either numeric or alphanumeric
    external_tracker_url: External Issue Tracker URL.

    """

    external_tracker_format: str
    external_tracker_style: str
    external_tracker_url: str


@dataclass
class ExternalWikiModel:
    """ExternalWiki represents setting for external wiki.

    external_wiki_format: URL of external wiki.
    """

    external_wiki_url: str


@dataclass
class InternalTrackerModel:
    """InternalTracker represents settings for internal tracker

    allow_only_contributors_to_track_time: Let only contributors track time (Built-in issue tracker)
    enable_issue_dependencies: Enable dependencies for issues and pull requests (Built-in issue tracker)
    enable_issue_links: Enable issue links (Built-in issue tracker)
    """

    allow_only_contributors_to_track_time: bool
    enable_issue_dependencies: bool
    enable_timetracking: bool


@dataclass
class PermissionModel:
    """Permission represents a set of permissions"""

    admin: bool
    push: bool
    pull: bool


@dataclass
class OrganizationModel:
    avatar_url: str
    description: str
    full_name: str
    id: int
    location: str
    repo_admin_change_team_access: bool
    username: str
    visibility: str
    website: str


@dataclass
class TeamModel:
    """Team represents a team in an organization"""

    can_create_org_repo: bool
    description: str
    id: int
    includes_all_repositories: bool
    name: str
    organization: OrganizationModel
    permission: str  # none, read, write, admin, owner
    units: str
    units_map: str


@dataclass
class RepoTransferModel:
    """RepoTransfer represents a pending repo transfer"""

    doer: UserModel
    recipient: UserModel
    teams: TeamModel


@dataclass
class RepositoryModel:
    # TODO: Fix external_tracker, external_wiki and internal_tracker
    allow_merge_commits: bool
    allow_rebase: bool
    allow_rebase_explicit: bool
    allow_squash_merge: bool
    archived: bool
    avatar_url: str
    clone_url: str
    created_at: str  # TODO: Change to datetime
    default_branch: str
    default_merge_style: str
    description: str
    empty: bool
    # external_tracker: ExternalTrackerModel
    # external_wiki: ExternalWikiModel
    fork: bool
    forks_count: int
    full_name: str
    has_issues: bool
    has_projects: bool
    has_pull_requests: bool
    has_wiki: bool
    html_url: str
    id: int
    ignore_whitespace_conflicts: bool
    internal: bool
    # internal_tracker: InternalTrackerModel
    language: str
    languages_url: str
    mirror: bool
    mirror_interval: str
    mirror_updated: str  # TODO: Change to datetime
    name: str
    open_issues_count: int
    open_pr_counter: int
    original_url: str
    owner: UserModel
    parent: str  # TODO: What is this?
    permissions: PermissionModel
    private: bool
    release_counter: int
    repo_transfer: RepoTransferModel
    size: int
    ssh_url: str
    stars_count: int
    template: bool
    updated_at: str  # TODO: Change to datetime
    watchers_count: int
    website: str


@dataclass
class SettingsModel:
    """User settings

    #TODO: There is a random bold Privacy in the middle of UserSettings in Swagger. Fix this?
    """

    description: str
    diff_view_style: str
    full_name: str
    hide_activity: bool
    hide_email: bool
    language: str
    location: str
    theme: str
    website: str


@dataclass
class OAuth2ApplicationModel:
    """OAuth2Application represents an OAuth2 application.

    Attributes:
        client_id: The client ID.
        client_secret: The client secret.
        created: The date the application was created.
    """

    client_id: str
    client_secret: str
    created_at: str  # TODO: Change to datetime
    id: int
    name: str
    redirect_uris: List[str]


@dataclass
class GPGKeyEmailModel:
    """An email attached to a GPGKey."""

    email: str
    verified: bool


@dataclass
class GPGKeyModel:
    """A user GPG key to sign commit and tag in repository"""

    # TODO: Subkeys has a lot of stuff in it that is hidden in Swagger. Fix this?
    can_certify: bool
    can_encrypt_comms: bool
    can_encrypt_storage: bool
    can_sign: bool
    created_at: str
    emails: List[GPGKeyEmailModel]
    expires_at: str  # TODO: Change to datetime
    id: int
    key_id: str
    primary_key_id: str
    public_key: str
    subkeys: List[str]
    verified: bool


@dataclass
class CronModel:
    """A cron task"""

    exec_times: int
    name: str
    next: str  # TODO: Change to datetime
    prev: str  # TODO: Change to datetime
    schedule: str
