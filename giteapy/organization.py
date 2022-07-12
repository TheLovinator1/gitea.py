from giteapy.gitea import Gitea


class Organization(Gitea):
    def list_organizations(self, page: int, limit: int):
        # TODO: Implement me
        raise NotImplementedError

    def create_organization(
        self,
        username: str,
        description: str,
        full_name: str,
        location: str,
        repo_admin_change_team_access: bool,
        visibility: str,  # public, private, internal
        website: str,
    ):
        # TODO: Implement me
        raise NotImplementedError

    def get_organization(self, username: str):
        # TODO: Implement me
        raise NotImplementedError

    def delete_organization(self, username: str):
        # TODO: Implement me
        raise NotImplementedError

    def edit_organization(
        self,
        username: str,
        description: str,
        full_name: str,
        location: str,
        repo_admin_change_team_access: bool,
        visibility: str,  # public, private, internal
        website: str,
    ):
        # TODO: Implement me
        raise NotImplementedError

    def list_organization_webhooks(self, organization: str, page: int, limit: int):
        # TODO: Implement me
        raise NotImplementedError

    def create_organization_webhook(
        self,
        organization: str,
        active: bool,
        branch_filter: str,
        config: str,  # TODO: Make dataclass
        events: bool,
        # dingtalk, discord, gitea, gogs, msteams, slack, telegram, feishu, wechatwork, packagist
        type: str,  # TODO: Make dataclass
    ):
        # TODO: Implement me
        raise NotImplementedError

    def get_webhook(self, organization: str, webhook_id: int):
        # TODO: Implement me
        raise NotImplementedError

    def delete_webhook(self, organization: str, webhook_id: int):
        # TODO: Implement me
        raise NotImplementedError

    def update_hook(
        self,
        organization: str,
        webhook_id: int,
        active: bool,
        branch_filter: str,
        config: str,  # TODO: Not actually a str but a nice dataclass
        events: bool,
    ):
        # TODO: Implement me
        raise NotImplementedError

    def list_organization_label(self, organization: str, page: int, limit: int):
        # TODO: Implement me
        raise NotImplementedError

    def crete_organization_label(
        self, organization: str, name: str, color: str, description: str
    ):
        # TODO: Implement me
        raise NotImplementedError

    def get_label(self, organization: str, label_id: int):
        # TODO: Implement me
        raise NotImplementedError

    def delete_label(self, organization: str, label_id: int):
        # TODO: Implement me
        raise NotImplementedError

    def update_label(
        self,
        organization: str,
        label_id: int,
        name: str,
        color: str,
        description: str,
    ):
        # TODO: Implement me
        raise NotImplementedError

    def list_organization_members(self, organization: str, page: int, limit: int):
        # TODO: Implement me
        raise NotImplementedError

    def if_member_in_organization(self, organization: str, username: str):
        # TODO: Implement me
        raise NotImplementedError

    def remove_member_from_organization(self, organization: str, username: str):
        # TODO: Implement me
        raise NotImplementedError

    def list_organization_members_public(
        self, organization: str, page: int, limit: int
    ):
        # TODO: Implement me
        raise NotImplementedError

    def if_member_in_organization_public(self, organization: str, username: str):
        # TODO: Implement me
        raise NotImplementedError

    def make_member_public(self, organization: str, username: str):
        # TODO: Implement me
        raise NotImplementedError

    def make_member_private(self, organization: str, username: str):
        # TODO: Implement me
        raise NotImplementedError

    def list_organization_repositories(self, organization: str, page: int, limit: int):
        # TODO: Implement me
        raise NotImplementedError

    def create_repo_in_organization(
        self,
        organization: str,
        auto_init: bool,
        default_branch: str,
        description: str,
        gitignores: str,
        issue_labels: str,
        license: str,
        name: str,
        private: bool,
        readme: str,
        template: bool,
        trust_model: str,  # default, collaborator, committer, collaboratorcommitter
    ):
        # TODO: Implement me
        raise NotImplementedError

    def list_organization_teams(self, organization: str, page: int, limit: int):
        # TODO: Implement me
        raise NotImplementedError

    def create_team_in_organization(
        self,
        organization: str,
        can_create_org_repo: bool,
        description: str,
        includes_all_repositories: bool,
        name: str,
        permission: str,  # read, write, admin
        # List [ "repo.code", "repo.issues", "repo.ext_issues", "repo.wiki", "repo.pulls", "repo.releases", "repo.projects", "repo.ext_wiki" ]
        units: str,  # TODO: Make UnitsModel ^^^
        units_map: str,  # {"repo.code":"read","repo.issues":"write","repo.ext_issues":"none","repo.wiki":"admin","repo.pulls":"owner","repo.releases":"none","repo.projects":"none","repo.ext_wiki":"none"]
    ):
        # TODO: Implement me
        raise NotImplementedError

    def search_teams_in_organization(
        self, organization: str, query: str, include_desc: bool, page: int, limit: int
    ):
        # TODO: Implement me
        raise NotImplementedError

    def get_team(self, team_id: int):
        # TODO: Implement me
        raise NotImplementedError

    def delete_team(self, team_id: int):
        # TODO: Implement me
        raise NotImplementedError

    def update_team(
        self,
        team_id: int,
        can_create_org_repo: bool,
        description: str,
        includes_all_repositories: bool,
        name: str,
        permission: str,  # read, write, admin
        # List [ "repo.code", "repo.issues", "repo.ext_issues", "repo.wiki", "repo.pulls", "repo.releases", "repo.projects", "repo.ext_wiki" ]
        units: str,  # TODO: Make UnitsModel ^^^
        units_map: str,  # {"repo.code":"read","repo.issues":"write","repo.ext_issues":"none","repo.wiki":"admin","repo.pulls":"owner","repo.releases":"none","repo.projects":"none","repo.ext_wiki":"none"}
    ):
        # TODO: Implement me
        raise NotImplementedError

    def list_team_members(self, team_id: int, page: int, limit: int):
        # TODO: Implement me
        raise NotImplementedError

    def get_member_in_team(self, team_id: int, username: str):
        # TODO: Implement me
        raise NotImplementedError

    def add_team_member(self, team_id: int, username: str):
        # TODO: Implement me
        raise NotImplementedError

    def remove_team_member(self, team_id: int, username: str):
        # TODO: Implement me
        raise NotImplementedError

    def list_team_repositories(self, team_id: int, page: int, limit: int):
        # TODO: Implement me
        raise NotImplementedError

    def get_repository_in_team(self, team_id: int, organization: str, repository: str):
        # TODO: Implement me
        raise NotImplementedError

    def add_repository_to_team(self, team_id: int, organization: str, repository: str):
        # TODO: Implement me
        raise NotImplementedError

    def remove_repository_from_team(
        self, team_id: int, organization: str, repository: str
    ):
        # TODO: Implement me
        raise NotImplementedError

    def list_current_users_organizations(self, page: int, limit: int):
        # TODO: Implement me
        raise NotImplementedError

    def list_users_organizations(self, username: str, page: int, limit: int):
        # TODO: Implement me
        raise NotImplementedError

    def get_user_permissions(self, username: str, organization: str):
        # TODO: Implement me
        raise NotImplementedError
