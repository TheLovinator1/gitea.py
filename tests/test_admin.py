import pytest
from giteapy.gitea import Gitea
from giteapy.admin import Admin


def test_cron_tasks():
    with Gitea(url=pytest.url, token=pytest.token, log_level="DEBUG") as gitea:
        tasks = Admin.cron_tasks(gitea, page=1, limit=100)
        for task in tasks:
            assert hasattr(task, "exec_times")
            assert type(task.exec_times) is int

            assert hasattr(task, "name")
            assert type(task.name) is str

            assert hasattr(task, "next")
            assert type(task.next) is str

            assert hasattr(task, "prev")
            assert type(task.prev) is str

            assert hasattr(task, "schedule")
            assert type(task.schedule) is str
