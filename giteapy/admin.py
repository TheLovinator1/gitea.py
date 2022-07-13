from typing import Generator
from giteapy.gitea import Gitea
from giteapy.models import CronModel
from giteapy.exceptions import APIForbiddenError


class Admin(Gitea):
    def cron_tasks(self, page: int, limit: int) -> Generator[CronModel, None, None]:
        """List cron tasks. Also called cron jobs.

        Args:
            page: Page number (1-based).
            limit: How many results to return per page

        Yields:
            CronModel: The cron task.

        Raises:
            APIForbiddenError: If the user is not an admin.
        """
        path = "/admin/cron"

        params = {"page": page, "limit": limit}
        request = self.get_request(path, params)
        data = request.data

        if request.response.status_code == 200:
            for task in data:
                yield CronModel(
                    exec_times=task["exec_times"],
                    name=task["name"],
                    next=task["next"],
                    prev=task["prev"],
                    schedule=task["schedule"],
                )
        elif request.response.status_code == 403:
            # TODO: Run test as non-admin user and check that this error is raised.
            raise APIForbiddenError(message=data["message"], url=data["url"])

    def run_cron_task(self, task: str):
        raise NotImplementedError

    def list_all_organizations(self, page: int, limit: int):
        raise NotImplementedError

    def list_unadopted_repositories(self, page: int, limit: int, pattern: str):
        raise NotImplementedError

    def adopt_unadopted_files(self, owner: str, repo: str):
        raise NotImplementedError

    def delete_unadopted_files(self, owner: str, repo: str):
        raise NotImplementedError

    def list_all_users(self, page: int, limit: int):
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
        raise NotImplementedError

    def delete_a_user(self):
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
        raise NotImplementedError

    def add_a_public_key(self, username: str, key: str, read_only: bool, title: str):
        raise NotImplementedError

    def delete_a_public_key(self, username: str, key_id: int):
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
        raise NotImplementedError
