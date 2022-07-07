from dataclasses import dataclass
import logging
import typing
import httpx
import json
from httpx._types import QueryParamTypes


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

    @dataclass
    class RequestModel:
        response: httpx.Response
        response_text: typing.Any

    def get_request(
        self,
        path: str,
        params: typing.Optional[QueryParamTypes] = None,
        silence_404: bool = False,
    ) -> RequestModel:
        """Do a GET request to the API.

        Args:
            path: The path to the API endpoint.
            params (optional): Defaults to None.
            silence_404 (optional): _description_. Defaults to False.

        Returns:
            RequestModel: The HTTP response from Gitea.
        """
        try:
            self.logger.debug(f"GET {path} with params {params}")
            response: httpx.Response
            response = self.client.get(url=self.url + path, params=params)
            response.raise_for_status()

        except httpx.RequestError as exc:
            url = exc.request.url
            self.logger.error(f"An error occurred while requesting {url!r}.")

        except httpx.HTTPStatusError as exc:
            # Silence 404 errors when we know they are not relevant
            if exc.response.status_code == 404 and not silence_404:
                status_code = exc.response.status_code
                url = exc.request.url
                self.logger.error(f"Error {status_code} while requesting {url!r}.")

        if response.text:
            return self.RequestModel(response, json.loads(response.text))
        return self.RequestModel(response, "")

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

            if exc.response.status_code == 401:
                self.logger.error(f"{response}")

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
