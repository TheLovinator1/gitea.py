from giteapy.gitea import Gitea

from giteapy.models import UserModel, EmailListModel
from typing import Generator


class User(Gitea):
    def get_user(self) -> UserModel:
        """Get the authenticated user."""
        path = "/user"
        request = self.get_request(path)
        data = request.response_text

        return UserModel(
            active=data["active"],
            avatar_url=data["avatar_url"],
            created=data["created"],
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

    def get_emails(self) -> Generator[EmailListModel, None, None]:
        """Get the authenticated user's email addresses.

        Yields:
            EmailListModel: The user's email addresses.
        """
        path = "/user/emails"
        request = self.get_request(path)
        data = request.response_text

        for email in data:
            yield EmailListModel(
                email=email["email"],
                verified=email["verified"],
                primary=email["primary"],
            )

    def get_followers(self, page, limit):
        """Get the authenticated user's followers.

        Args:
            page (int): The page number.
            limit (int): The number of items per page.

        Yields:
            UserModel: The user's followers.

        # TODO: Implement pagination and always get max limit if limit is unspecified.
        """
        path = "/user/followers"
        request = self.get_request(path=path, params={"page": page, "limit": limit})
        data = request.response_text

        for user in data:
            yield UserModel(
                active=user["active"],
                avatar_url=user["avatar_url"],
                created=user["created"],
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

    def get_following(self, page, limit):
        """Get the authenticated user's following.

        Args:
            page (int): The page number.
            limit (int): The number of items per page.

        Yields:
            UserModel: The user's following.

        # TODO: Implement pagination and always get max limit if limit is unspecified.
        """
        path = "/user/following"
        request = self.get_request(path, {"page": page, "limit": limit})
        data = request.response_text

        for user in data:
            yield UserModel(
                active=user["active"],
                avatar_url=user["avatar_url"],
                created=user["created"],
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

    def get_if_following_username(self, username: str) -> bool:
        """Check if the authenticated user is following the given username.

        Args:
            username (str): The username of the user to check.

        Returns:
            bool: True if we are following the user, False otherwise.
        """
        path = f"/user/following/{username}"

        # If user is not following, the request will return a 404.
        # We need to silence that.
        request = self.get_request(path, silence_404=True)
        data = request.response_text
        self.logger.debug(f"data: {data}")

        if data:
            if "The target couldn't be found." in data["message"]:
                return False
        return True
