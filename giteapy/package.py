from giteapy.gitea import Gitea


class Package(Gitea):
    def get_packages(self, owner: str, page: int, limit: int, type: str, query: str):
        raise NotImplementedError

    def get_package(self, owner: str, type: str, name: str, version: str):
        raise NotImplementedError

    def delete_package(self, owner: str, type: str, name: str, version: str):
        raise NotImplementedError

    def get_all_files(self, owner: str, type: str, name: str, version: str):
        raise NotImplementedError
