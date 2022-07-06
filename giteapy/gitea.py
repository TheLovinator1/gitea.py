import logging
import httpx
import json


class Gitea:
    def __init__(self, url: str, token: str, log_level="INFO") -> None:
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)

        # Append the API path to the URL if not exists
        if not url.endswith("/api/v1/"):
            url += "/api/v1/"

        # Remove the trailing slash from the URL
        if url.endswith("/"):
            url = url[:-1]

        self.url = url
        self.token = token
        self.headers = {"Authorization": f"token {token}"}

    def __enter__(self):
        """This is for the 'with' thingy."""
        self.client = httpx.Client(headers=self.headers, base_url=self.url)
        self.logger.debug(f"Connected to {self.url}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.client.close()
        self.logger.debug(f"Disconnected from {self.url}")
        return False

    def get_request(
        self,
        path: str,
        params=None,
        error_404: str = "HTTP 404 Not Found",
    ):
        try:
            self.logger.debug(f"GET {path} with params {params}")
            response: httpx.Response
            response = self.client.get(url=self.url + path, params=params)

            # Raise HTTPStatusError if the response is not 200
            response.raise_for_status()

        except httpx.RequestError as exc:
            self.logger.error(
                f"An error occurred while requesting {exc.request.url!r}.",
                exc_info=True,
            )

        except httpx.HTTPStatusError as exc:
            self.logger.error(
                f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.",
                exc_info=True,
            )
            if exc.response.status_code == 404:
                self.logger.error(f"{error_404}")

        return json.loads(response.text)

    def post_request(
        self,
        path: str,
        error_400: str = "HTTP 400 Bad Request",
        error_403: str = "HTTP 403 Forbidden",
        error_404: str = "HTTP 404 Not Found",
        error_409: str = "HTTP 409 Conflict",
        error_422: str = "HTTP 422 Unprocessable Entity",
    ):
        try:
            self.logger.debug(f"GET {path}")
            response: httpx.Response = self.client.get(self.url + path)

            # Raise HTTPStatusError if the response is not 200
            response.raise_for_status()

        except httpx.RequestError as exc:
            self.logger.error(
                f"An error occurred while requesting {exc.request.url!r}.",
                exc_info=True,
            )
            return False

        except httpx.HTTPStatusError as exc:
            self.logger.error(
                f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.",
                exc_info=True,
            )

            # 400 Bad Request
            if exc.response.status_code == 400:
                self.logger.error(f"{error_400}")

            # 403 Forbidden
            if exc.response.status_code == 403:
                self.logger.error(f"{error_403}")

            # 404 Not Found
            if exc.response.status_code == 404:
                self.logger.error(f"{error_404}")

            # 409 Conflict
            if exc.response.status_code == 409:
                self.logger.error(f"{error_409}")

            # 422 Unprocessable Entity
            if exc.response.status_code == 422:
                self.logger.error(f"{error_422}")

            return False

        return json.loads(response.text)

    def put_request(self):
        pass

    def delete_request(self):
        pass
