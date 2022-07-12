from giteapy.gitea import Gitea


class Miscellaneous(Gitea):
    def list_users_notification_threads(
        self, show_read: bool, status_types: str, subject_type: str, since: str, before: str, page: int, limit: int
    ):
        raise NotImplementedError

    def notification_mark_as_read(self, last_read_at: str, to_status: str, all: bool, status_types: str = "read"):
        raise NotImplementedError

    def notification_mark_as_unread(self, last_read_at: str, to_status: str, all: bool, status_types: str = "unread"):
        raise NotImplementedError

    def notification_mark_as_pinned(self, last_read_at: str, to_status: str, all: bool, status_types: str = "pinned"):
        raise NotImplementedError

    def if_unread_notification(self):
        raise NotImplementedError

    def get_notification_thread(self, thread_id: int):
        raise NotImplementedError

    def mark_notification_thread_as_read(self, thread_id: int, to_status: str):
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
        raise NotImplementedError

    def mark_notification_thread_as_read_on_repo(
        self, owner: str, repo: str, all: bool, status_types: str, to_status: str, last_read_at: str
    ):
        raise NotImplementedError
