from giteapy.gitea import Gitea

from giteapy.models import UserModel, EmailListModel
from typing import Generator


class User(Gitea):
    def get_user(self) -> UserModel:
        """Get the authenticated user."""
        path = "/user"
        data = self.get_request(path=path)

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
        data = self.get_request(path=path)

        for email in data:
            yield EmailListModel(
                email=email["email"],
                verified=email["verified"],
                primary=email["primary"],
            )
