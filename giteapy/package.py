from giteapy.gitea import Gitea


class Package(Gitea):
    def get_packages(
        self,
        owner: str,
        page: int,
        limit: int,
        type: str,  # composer, conan, container, generic, helm, maven, npm, nuget, pypi, rubygems
        query: str,
    ):
        # TODO: Implement me
        raise NotImplementedError

    def get_package(self, owner: str, type: str, name: str, version: str):
        # TODO: Implement me
        raise NotImplementedError

    def delete_package(self, owner: str, type: str, name: str, version: str):
        # TODO: Implement me
        raise NotImplementedError

    def get_all_files(self, owner: str, type: str, name: str, version: str):
        # TODO: Implement me
        raise NotImplementedError
