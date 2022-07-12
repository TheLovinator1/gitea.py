from typing import List
from giteapy.gitea import Gitea


class Issue(Gitea):
    def search_issues(
        self,
        state: str,
        labels: str,
        milestones: str,
        query: str,
        priority_repo_id: int,
        type: str,
        since: str,
        before: str,
        assigned: bool,
        created: bool,
        mentioned: bool,
        review_requested: bool,
        owner: str,
        team: str,
        page: int,
        limit: int,
    ):
        raise NotImplementedError

    def list_issues(
        self,
        owner: str,
        repo: str,
        state: str,
        labels: str,
        query: str,
        type: str,
        milestone: str,
        since: str,
        before: str,
        created_by: str,
        assigned_by: str,
        mentioned_by: str,
        page: int,
        limit: int,
    ):
        raise NotImplementedError

    def create_issue(
        self,
        owner: str,
        repo: str,
        assignees: str,  # AssigneesModel
        body: str,
        closed: bool,
        due_date: str,
        labels: List[str],  # LabelModel
        milestone: str,
        ref: str,
        title: str,
    ):
        raise NotImplementedError

    def list_all_comments(self, owner: str, repo: str, since: str, before: str, page: int, limit: int):
        raise NotImplementedError

    def get_comment(self, owner: str, repo: str, comment_id: int):
        raise NotImplementedError

    def delete_comment(self, owner: str, repo: str, comment_id: int):
        raise NotImplementedError

    def edit_comment(self, owner: str, repo: str, comment_id: int, body: str):
        raise NotImplementedError

    def get_reactions(self, owner: str, repo: str, comment_id: int):
        raise NotImplementedError

    def add_reaction(self, owner: str, repo: str, comment_id: int, reaction: str):
        raise NotImplementedError

    def remove_reaction(self, owner: str, repo: str, comment_id: int, reaction: str):
        raise NotImplementedError

    def get_issue(self, owner: str, repo: str, index: int):
        raise NotImplementedError

    def delete_issue(self, owner: str, repo: str, index: int):
        raise NotImplementedError

    def edit_issue(
        self,
        owner: str,
        repo: str,
        index: int,
        assignees: List[str],  # AssigneesModel
        body: str,
        due_date: str,
        milestone: str,
        ref: str,
        state: str,
        title: str,
        unset_due_date: bool,
    ):
        raise NotImplementedError

    def list_comments(self, owner: str, repo: str, index: int, since: str, before: str):
        raise NotImplementedError

    def add_comment(self, owner: str, repo: str, index: int, body: str):
        raise NotImplementedError

    def set_deadline(self, owner: str, repo: str, index: int, due_date: str):
        raise NotImplementedError

    def delete_deadline(self, owner: str, repo: str, index: int, due_date: str):
        raise NotImplementedError

    def get_labels(self, owner: str, repo: str, index: int):
        raise NotImplementedError

    def replace_labels(self, owner: str, repo: str, index: int, labels: List[int]):
        raise NotImplementedError

    def add_label(self, owner: str, repo: str, index: int, label: str):
        raise NotImplementedError

    def remove_all_labels(self, owner: str, repo: str, index: int):
        raise NotImplementedError

    def remove_label(self, owner: str, repo: str, index: int, label: str):
        raise NotImplementedError

    def delete_stopwatch(self, owner: str, repo: str, index: int):
        raise NotImplementedError

    def start_stopwatch(self, owner: str, repo: str, index: int):
        raise NotImplementedError

    def stop_stopwatch(self, owner: str, repo: str, index: int):
        raise NotImplementedError

    def get_subscribers(self, owner: str, repo: str, index: int, page: int, limit: int):
        raise NotImplementedError

    def if_subscribed(self, owner: str, repo: str, index: int, user: str):
        raise NotImplementedError

    def subscribe(self, owner: str, repo: str, index: int, user: str):
        raise NotImplementedError

    def unsubscribe(self, owner: str, repo: str, index: int, user: str):
        raise NotImplementedError

    def list_comments_and_events(
        self, owner: str, repo: str, index: int, since: str, page: int, limit: int, before: str
    ):
        raise NotImplementedError

    def list_tracked_times(
        self, owner: str, repo: str, index: int, user: str, since: str, before: str, page: int, limit: int
    ):
        raise NotImplementedError

    def add_tracked_time(self, owner: str, repo: str, index: int, created: str, time: str, username: str):
        raise NotImplementedError

    def reset_tracked_time(self, owner: str, repo: str, index: int):
        raise NotImplementedError

    def delete_tracked_time(self, owner: str, repo: str, index: int, id: int):
        raise NotImplementedError

    def get_repository_labels(self, owner: str, repo: str, page: int, limit: int):
        raise NotImplementedError

    def create_label(self, owner: str, repo: str, color: str, description: str, name: str):
        raise NotImplementedError

    def get_label(self, owner: str, repo: str, label_id: int):
        raise NotImplementedError

    def delete_label(self, owner: str, repo: str, label_id: int):
        raise NotImplementedError

    def update_label(self, owner: str, repo: str, label_id: int, color: str, description: str, name: str):
        raise NotImplementedError

    def list_milestones(self, owner: str, repo: str, state: str, name: str, page: int, limit: int):
        raise NotImplementedError

    def create_milestone(self, owner: str, repo: str, description: str, due_on: str, state: str, title: str):
        raise NotImplementedError

    def get_milestone(self, owner: str, repo: str, milestone_id: int):
        raise NotImplementedError

    def delete_milestone(self, owner: str, repo: str, milestone_id: int):
        raise NotImplementedError

    def update_milestone(
        self, owner: str, repo: str, milestone_id: int, description: str, due_on: str, state: str, title: str
    ):
        raise NotImplementedError
