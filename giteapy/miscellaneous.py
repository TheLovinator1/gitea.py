from giteapy.gitea import Gitea


class Miscellaneous(Gitea):
    def render_md_document_as_html(
        self, context: str, mode: str, text: str, wiki: bool
    ):
        # TODO: Implement me
        raise NotImplementedError

    def render_raw_md_as_html(self, text: str):
        # TODO: Implement me
        raise NotImplementedError

    def return_nodeinfo(self):
        # TODO: Implement me
        raise NotImplementedError

    def get_default_signing_key_gpg(self):
        # TODO: Implement me
        raise NotImplementedError

    def gitea_version(self):
        # TODO: Implement me
        raise NotImplementedError
