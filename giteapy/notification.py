from giteapy.gitea import Gitea


class Miscellaneous(Gitea):
    def list_users_notification_threads(
        self,
        show_read: bool,
        status_types: str,  # unread, read and/or pinned
        subject_type: str,  # issue, pull, commit, repository
        since: str,
        before: str,
        page: int,
        limit: int,
    ):
        # TODO: Implement me
        raise NotImplementedError

    def notification_mark_as_read(
        self,
        last_read_at: str,
        to_status: str,
        status_types: str = "read",
        all: bool = False,  # TODO: This is str on swagger, but it should be bool?
    ):
        # TODO: Implement me
        raise NotImplementedError

    def notification_mark_as_unread(
        self,
        last_read_at: str,
        to_status: str,
        status_types: str = "unread",
        all: bool = False,  # TODO: This is str on swagger, but it should be bool?
    ):
        # TODO: Implement me
        raise NotImplementedError

    def notification_mark_as_pinned(
        self,
        last_read_at: str,
        to_status: str,
        status_types: str = "pinned",
        all: bool = False,  # TODO: This is str on swagger, but it should be bool?
    ):
        # TODO: Implement me
        raise NotImplementedError

    def if_unread_notification(self):
        # TODO: Implement me
        raise NotImplementedError

    def get_notification_thread(self, thread_id: int):
        # TODO: Implement me
        raise NotImplementedError

    def mark_notification_thread_as_read(self, thread_id: int, to_status: str):
        # TODO: Implement me
        raise NotImplementedError

    def list_users_notification_threads_on_repo(
        self,
        owner: str,
        repo: str,
        all: bool,
        status_types: str,
        subject_type: str,
        since: str,
        before: str,
        page: int,
        limit: int,
    ):
        # TODO: Implement me
        raise NotImplementedError

    def mark_notification_thread_as_read_on_repo(
        self,
        owner: str,
        repo: str,
        all: bool,
        status_types: str,  # unread, read and/or pinned
        to_status: str,
        last_read_at: str,
    ):
        # TODO: Implement me
        raise NotImplementedError
