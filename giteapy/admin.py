from giteapy.gitea import Gitea


class Admin(Gitea):
    def list_cron_tasks(self, page: int, limit: int):
        # TODO: Implement me
        raise NotImplementedError

    def run_cron_task(self, task: str):
        # TODO: Implement me
        raise NotImplementedError

    def list_all_organizations(self, page: int, limit: int):
        # TODO: Implement me
        raise NotImplementedError

    def list_unadopted_repositories(self, page: int, limit: int, pattern: str):
        # TODO: Implement me
        raise NotImplementedError

    def adopt_unadopted_files(self, owner: str, repo: str):
        # TODO: Implement me
        raise NotImplementedError

    def delete_unadopted_files(self, owner: str, repo: str):
        # TODO: Implement me
        raise NotImplementedError

    def list_all_users(self, page: int, limit: int):
        # TODO: Implement me
        raise NotImplementedError

    def create_user(
        self,
        email: str,
        full_name: str,
        login_name: str,
        must_change_password: bool,
        password: str,
        restricted: bool,
        send_notify: bool,
        source_id: int,
        username: str,
        visibility: str,  # public, private, internal
    ):
        # TODO: Implement me
        raise NotImplementedError

    def delete_a_user(self):
        # TODO: Implement me
        raise NotImplementedError

    def edit_a_user(
        self,
        username: str,
        active: bool,
        admin: bool,
        allow_create_organization: bool,
        allow_git_hook: bool,
        allow_import_local: bool,
        description: str,
        email: str,
        full_name: str,
        location: str,
        login_name: str,
        max_repo_creation: int,
        must_change_password: bool,
        password: str,
        prohibit_login: bool,
        restricted: bool,
        source_id: int,
        visibility: str,  # public, private, internal
        website: str,
    ):
        # TODO: Implement me
        raise NotImplementedError

    def add_a_public_key(self, username: str, key: str, read_only: bool, title: str):
        # TODO: Implement me
        raise NotImplementedError

    def delete_a_public_key(self, username: str, key_id: int):
        # TODO: Implement me
        raise NotImplementedError

    def create_a_organization(
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

    def create_repo_for_user(
        self,
        username: str,
        auto_init: bool,
        default_branch: str,
        description: str,
        gitignores: str,
        issue_labels: str,
        license: str,
        name: str,
        private: bool,
        readme: str,
        template: str,
        trust_model: str,  # default, collaborator, committer, collaboratorcommitter
    ):
        # TODO: Implement me
        raise NotImplementedError
