from giteapy.gitea import Gitea

from giteapy.models import (
    GPGKeyModel,
    UserModel,
    EmailListModel,
    RepositoryModel,
    SettingsModel,
    OAuth2ApplicationModel,
)
from typing import Generator, List
from giteapy.exceptions import OAuth2ApplicationNotFound, UserNotFound


class User(Gitea):
    def get_user(self, username: str = None) -> UserModel:
        """Get a user by username.

        Args:
            username: If specified, get username's user instead of the authenticated user's.

        Returns:
            UserModel: The user.
        """
        path = "/user"

        if username:
            path = f"/users/{username}"
            self.logger.info(f"Getting user {username}")

        request = self.get_request(path)
        data = request.data

        return UserModel(
            active=data["active"],
            avatar_url=data["avatar_url"],
            created_at=data["created"],
            description=data["description"],
            email=data["email"],
            followers_count=data["followers_count"],
            following_count=data["following_count"],
            full_name=data["full_name"],
            id=data["id"],
            is_admin=data["is_admin"],
            language=data["language"],
            last_login=data["last_login"],
            location=data["location"],
            login=data["login"],
            prohibit_login=data["prohibit_login"],
            restricted=data["restricted"],
            starred_repos_count=data["starred_repos_count"],
            visibility=data["visibility"],
            website=data["website"],
        )

    def get_oauth2_applications(self, page: int, limit: int):
        path = "/user/applications/oauth2"

        request = self.get_request(path, {"page": page, "limit": limit})
        data = request.data

        for app in data:
            yield OAuth2ApplicationModel(
                client_id=app["client_id"],
                client_secret=app["client_secret"],
                created_at=app["created"],
                id=app["id"],
                name=app["name"],
                redirect_uris=app["redirect_uris"],
            )

    def create_oauth2_application(self, name: str, redirect_uris: List[str]):
        raise NotImplementedError

    def get_oauth2_application_by_id(self, id: int):
        """Get an OAuth2 application by its ID.

        Args:
            id (int): The ID of the OAuth2 application.

        Returns:
            OAuth2ApplicationModel: The OAuth2 application.
        """
        path = f"/user/applications/oauth2/{id}"

        request = self.get_request(path)
        data = request.data

        if hasattr(data, "message"):
            if "The target couldn't be found." in data["message"]:
                raise OAuth2ApplicationNotFound(id)

        return OAuth2ApplicationModel(
            client_id=data["client_id"],
            client_secret=data["client_secret"],
            created_at=data["created"],
            id=data["id"],
            name=data["name"],
            redirect_uris=data["redirect_uris"],
        )

    def delete_oauth2_application(self, id: int):
        raise NotImplementedError

    def update_oauth2_application(self, id: int, name: str, redirect_uris: List[str]):
        raise NotImplementedError

    def get_emails(self) -> Generator[EmailListModel, None, None]:
        """Get the authenticated user's email addresses.

        Yields:
            EmailListModel: The user's email addresses.
        """
        path = "/user/emails"

        request = self.get_request(path)
        data = request.data

        for email in data:
            yield EmailListModel(
                email=email["email"],
                verified=email["verified"],
                primary=email["primary"],
            )

    def add_new_email_address(self, email: str):
        raise NotImplementedError

    def delete_email_address(self, email: str):
        raise NotImplementedError

    def get_followers(self, page: int, limit: int, username: str = None):
        """Get the authenticated user's followers.

        Args:
            page (int): The page number.
            limit (int): The number of items per page.
            username: If specified, get username's followers instead of the authenticated user's.

        Yields:
            UserModel: The user's followers.

        # TODO: Implement pagination and always get max limit if limit is unspecified.
        """
        path = "/user/followers"

        if username:
            path = f"/users/{username}/followers"
            self.logger.info(f"Getting followers for user {username}")

        request = self.get_request(path=path, params={"page": page, "limit": limit})
        data = request.data

        for user in data:
            yield UserModel(
                active=user["active"],
                avatar_url=user["avatar_url"],
                created_at=user["created"],
                description=user["description"],
                email=user["email"],
                followers_count=user["followers_count"],
                following_count=user["following_count"],
                full_name=user["full_name"],
                id=user["id"],
                is_admin=user["is_admin"],
                language=user["language"],
                last_login=user["last_login"],
                location=user["location"],
                login=user["login"],
                prohibit_login=user["prohibit_login"],
                restricted=user["restricted"],
                starred_repos_count=user["starred_repos_count"],
                visibility=user["visibility"],
                website=user["website"],
            )

    def get_following(self, page: int, limit: int, username: str = None):
        """Get a list of users the authenticated user is following.

        Args:
            page: The page number.
            limit: The number of items per page.
            username: If specified, get username's followers instead of the authenticated user's.

        Yields:
            UserModel: The user's following.

        # TODO: Implement pagination and always get max limit if limit is
        unspecified.
        """
        path = "/user/following"

        if username:
            path = f"/users/{username}/following"
            self.logger.info(f"Getting user {username}")

        request = self.get_request(path, {"page": page, "limit": limit})
        data = request.data

        for user in data:
            yield UserModel(
                active=user["active"],
                avatar_url=user["avatar_url"],
                created_at=user["created"],
                description=user["description"],
                email=user["email"],
                followers_count=user["followers_count"],
                following_count=user["following_count"],
                full_name=user["full_name"],
                id=user["id"],
                is_admin=user["is_admin"],
                language=user["language"],
                last_login=user["last_login"],
                location=user["location"],
                login=user["login"],
                prohibit_login=user["prohibit_login"],
                restricted=user["restricted"],
                starred_repos_count=user["starred_repos_count"],
                visibility=user["visibility"],
                website=user["website"],
            )

    def if_following(self, username: str, target: str = None) -> bool:
        """Check if a user is following the given username.

        Args:
            username (str): Username of the following user.
            target: Username of the followed user. If not specified, the authenticated user is checked.

        Raises:
            UserNotFound: The user was not found.

        Returns:
            bool: True if we are following the user, False otherwise.
        """
        path = f"/user/following/{username}"

        if target:
            path = f"/users/{username}/following/{target}"
            self.logger.info(f"Getting user {username}")

        # If user is not following, the request will return a 404.
        # We need to silence that.
        request = self.get_request(path, silence_404=True)
        data = request.data
        self.logger.debug(f"response_text: {data}")

        # Request response is empty if user is following.
        if data:
            # If we are not following the user, the response text will be 'The target couldn't be found'.
            if "The target couldn't be found." in data["message"]:
                # TODO: Check if we should use something else here.
                return False

            if data["message"].startswith("user redirect does not exist"):
                raise UserNotFound(username)

            else:
                # If we get another response text, we should raise an exception.
                # TODO: Add more contact information to the exception.
                error_msg = (
                    "Unexpected response: \n"
                    f"Expected 'The target couldn't be found.' but got '{data}' instead.\n"
                    "Please report this issue on https://github.com/TheLovinator1/gitea.py or "
                    "https://git.lovinator.space/TheLovinator/gitea.py if this error persists."
                )
                self.logger.error(error_msg, exc_info=True)
                raise Exception(error_msg)
        return True

    def follow_user(self, username: str):
        raise NotImplementedError

    def unfollow_user(self, username: str):
        raise NotImplementedError

    def get_gpg_key_token(self) -> str:
        """Get the GPG key token for the authenticated user.

        Returns:
            str: The GPG key token.
        """
        # TODO: Need to implement when no gpg key is set.
        path = "/user/gpg_key_token"
        request = self.get_request(path)
        return request.data

    def verify_gpg_key_token(self, token: str) -> bool:
        raise NotImplementedError

    def get_gpg_keys(self, page: int, limit: int):
        """Get the authenticated user's GPG keys.

        Args:
            page (int): The page number.
            limit (int): The number of items per page.

        Yields:
            GPGKeyModel: The user's GPG keys.
        """
        path = "/user/gpg_keys"

        request = self.get_request(path, {"page": page, "limit": limit})
        data = request.data

        for gpg_key in data:
            yield GPGKeyModel(
                can_certify=gpg_key["can_certify"],
                can_encrypt_comms=gpg_key["can_encrypt_comms"],
                can_encrypt_storage=gpg_key["can_encrypt_storage"],
                can_sign=gpg_key["can_sign"],
                created_at=gpg_key["created_at"],
                emails=gpg_key["emails"],
                expires_at=gpg_key["expires_at"],
                id=gpg_key["id"],
                key_id=gpg_key["key_id"],
                primary_key_id=gpg_key["primary_key_id"],
                public_key=gpg_key["public_key"],
                subkeys=gpg_key["subkeys"],
                verified=gpg_key["verified"],
            )

    def create_gpg_key(self, armored_public_key: str, armored_signature: str):
        raise NotImplementedError

    def get_gpg_key_by_id(self, id: int):
        path = f"/user/gpg_keys/{id}"
        request = self.get_request(path)
        data = request.data

        # TODO: Implement when no gpg key is set.

        return GPGKeyModel(
            can_certify=data["can_certify"],
            can_encrypt_comms=data["can_encrypt_comms"],
            can_encrypt_storage=data["can_encrypt_storage"],
            can_sign=data["can_sign"],
            created_at=data["created_at"],
            emails=data["emails"],
            expires_at=data["expires_at"],
            id=data["id"],
            key_id=data["key_id"],
            primary_key_id=data["primary_key_id"],
            public_key=data["public_key"],
            subkeys=data["subkeys"],
            verified=data["verified"],
        )

    def remove_gpg_key(self, id: int):
        raise NotImplementedError

    def get_public_keys(self, fingerprint: str, page: int, limit: int, username: str = None):
        if username:
            # path = f"/users/{username}/keys"
            self.logger.info(f"Getting user {username}")

        raise NotImplementedError

    def create_public_key(self, key: str, read_only: bool, title: str):
        raise NotImplementedError

    def get_public_key_by_id(self, id: int):
        raise NotImplementedError

    def delete_public_key(self, id: int):
        raise NotImplementedError

    def get_repos(self, page: int, limit: int, username: str = None):
        """Get the authenticated user's repositories.

        Args:
            page: Page number of results to return (1-based)
            limit: The number of items per page.
            username: If specified, get username's user instead of the authenticated user's.


        Yields:
            RepositoryModel: The user's repositories.
        """

        path = "/user/repos"

        if username:
            path = f"/users/{username}/repos"
            self.logger.info(f"Getting user {username}")

        request = self.get_request(path, {"page": page, "limit": limit})
        data = request.data

        for repo in data:
            yield RepositoryModel(
                allow_merge_commits=repo["allow_merge_commits"],
                allow_rebase=repo["allow_rebase"],
                allow_rebase_explicit=repo["allow_rebase_explicit"],
                allow_squash_merge=repo["allow_squash_merge"],
                archived=repo["archived"],
                avatar_url=repo["avatar_url"],
                clone_url=repo["clone_url"],
                created_at=repo["created_at"],
                default_branch=repo["default_branch"],
                default_merge_style=repo["default_merge_style"],
                description=repo["description"],
                empty=repo["empty"],
                # external_tracker=repo["external_tracker"],
                # external_wiki=repo["external_wiki"],
                fork=repo["fork"],
                forks_count=repo["forks_count"],
                full_name=repo["full_name"],
                has_issues=repo["has_issues"],
                has_projects=repo["has_projects"],
                has_pull_requests=repo["has_pull_requests"],
                has_wiki=repo["has_wiki"],
                html_url=repo["html_url"],
                id=repo["id"],
                ignore_whitespace_conflicts=repo["ignore_whitespace_conflicts"],
                internal=repo["internal"],
                # internal_tracker=repo["internal_tracker"],
                language=repo["language"],
                languages_url=repo["languages_url"],
                mirror=repo["mirror"],
                mirror_interval=repo["mirror_interval"],
                mirror_updated=repo["mirror_updated"],
                name=repo["name"],
                open_issues_count=repo["open_issues_count"],
                open_pr_counter=repo["open_pr_counter"],
                original_url=repo["original_url"],
                owner=repo["owner"],
                parent=repo["parent"],
                permissions=repo["permissions"],
                private=repo["private"],
                release_counter=repo["release_counter"],
                repo_transfer=repo["repo_transfer"],
                size=repo["size"],
                ssh_url=repo["ssh_url"],
                stars_count=repo["stars_count"],
                template=repo["template"],
                updated_at=repo["updated_at"],
                watchers_count=repo["watchers_count"],
                website=repo["website"],
            )

    def create_repo(
        self,
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
        trust_model: str,
    ):
        raise NotImplementedError

    def get_settings(self):
        """Get the authenticated user's settings.

        Returns:
            SettingsModel: The user's settings.
        """
        path = "/user/settings"
        request = self.get_request(path)
        data = request.data

        return SettingsModel(
            description=data["description"],
            diff_view_style=data["diff_view_style"],
            full_name=data["full_name"],
            hide_activity=data["hide_activity"],
            hide_email=data["hide_email"],
            language=data["language"],
            location=data["location"],
            theme=data["theme"],
            website=data["website"],
        )

    def update_settings(
        self,
        description: str,
        diff_view_style: str,
        full_name: str,
        hide_activity: bool,
        hide_email: bool,
        language: str,
        location: str,
        theme: str,
        website: str,
    ):
        raise NotImplementedError

    def get_starred(self, page: int, limit: int, username: str = None):
        """Get repositories you have starred.

        Args:
            page (int): Page number of results to return (1-based)
            limit (int): The number of items per page.

        Yields:
            RepositoryModel: The user's starred repositories.
        """
        path = "/user/starred"

        if username:
            path = f"/users/{username}/starred"
            self.logger.info(f"Getting user {username}")

        request = self.get_request(path, {"page": page, "limit": limit})
        data = request.data

        for repo in data:
            yield RepositoryModel(
                allow_merge_commits=repo["allow_merge_commits"],
                allow_rebase=repo["allow_rebase"],
                allow_rebase_explicit=repo["allow_rebase_explicit"],
                allow_squash_merge=repo["allow_squash_merge"],
                archived=repo["archived"],
                avatar_url=repo["avatar_url"],
                clone_url=repo["clone_url"],
                created_at=repo["created_at"],
                default_branch=repo["default_branch"],
                default_merge_style=repo["default_merge_style"],
                description=repo["description"],
                empty=repo["empty"],
                # external_tracker=repo["external_tracker"],
                # external_wiki=repo["external_wiki"],
                fork=repo["fork"],
                forks_count=repo["forks_count"],
                full_name=repo["full_name"],
                has_issues=repo["has_issues"],
                has_projects=repo["has_projects"],
                has_pull_requests=repo["has_pull_requests"],
                has_wiki=repo["has_wiki"],
                html_url=repo["html_url"],
                id=repo["id"],
                ignore_whitespace_conflicts=repo["ignore_whitespace_conflicts"],
                internal=repo["internal"],
                # internal_tracker=repo["internal_tracker"],
                language=repo["language"],
                languages_url=repo["languages_url"],
                mirror=repo["mirror"],
                mirror_interval=repo["mirror_interval"],
                mirror_updated=repo["mirror_updated"],
                name=repo["name"],
                open_issues_count=repo["open_issues_count"],
                open_pr_counter=repo["open_pr_counter"],
                original_url=repo["original_url"],
                owner=repo["owner"],
                parent=repo["parent"],
                permissions=repo["permissions"],
                private=repo["private"],
                release_counter=repo["release_counter"],
                repo_transfer=repo["repo_transfer"],
                size=repo["size"],
                ssh_url=repo["ssh_url"],
                stars_count=repo["stars_count"],
                template=repo["template"],
                updated_at=repo["updated_at"],
                watchers_count=repo["watchers_count"],
                website=repo["website"],
            )

    def if_starred(self, owner: str, repo: str):
        raise NotImplementedError

    def star(self, owner: str, repo: str):
        raise NotImplementedError

    def unstar(self, owner: str, repo: str):
        raise NotImplementedError

    def stopwatches(self, page: int, limit: int):
        raise NotImplementedError

    def subscriptions(self, page: int, limit: int, username: str = None):
        raise NotImplementedError

    def teams(self, page: int, limit: int):
        raise NotImplementedError

    def times(self, page: int, limit: int):
        raise NotImplementedError

    def search_user(self, user_id: int, query: str, page: int, limit: int):
        raise NotImplementedError

    def heatmap(self, username: str):
        raise NotImplementedError

    def access_tokens(self, page: int, limit: int, username: str = None):
        raise NotImplementedError

    def create_access_token(self, token_name: str, username: str = None):
        raise NotImplementedError

    def delete_access_token(self, token_name: str, username: str = None):
        raise NotImplementedError
