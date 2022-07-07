from giteapy.gitea import Gitea

from giteapy.models import UserModel, EmailListModel
from typing import Generator
from giteapy.exceptions import UserNotFound


class User(Gitea):
    def get_user(self) -> UserModel:
        """Get the authenticated user."""
        path = "/user"
        request = self.get_request(path)
        data = request.data

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
        data = request.data

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
        data = request.data

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
        """Get a list of users the authenticated user is following.

        Args:
            page (int): The page number.
            limit (int): The number of items per page.

        Yields:
            UserModel: The user's following.

        # TODO: Implement pagination and always get max limit if limit is unspecified.
        """
        path = "/user/following"
        request = self.get_request(path, {"page": page, "limit": limit})
        data = request.data

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

    def if_following(self, username: str) -> bool:
        """Check if the authenticated user is following the given username.

        Args:
            username (str): The username of the user to check.

        Raises:
            UserNotFound: The user was not found.

        Returns:
            bool: True if we are following the user, False otherwise.
        """
        path = f"/user/following/{username}"

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
