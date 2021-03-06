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
        self.client = httpx.Client(
            headers=self.headers,
            base_url=self.url,
            event_hooks={
                "request": [self.log_request],
                "response": [self.log_response],
            },
        )
        self.logger.debug(f"Connected to {self.url}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.client.close()
        self.logger.debug(f"Disconnected from {self.url}")
        return False

    @dataclass
    class RequestModel:
        response: httpx.Response
        data: typing.Any

    def log_request(self, request):
        self.logger.debug(f"Request event hook: {request.method} {request.url} - Waiting for response")

    def log_response(self, response):
        request = response.request
        self.logger.debug(f"Response event hook: {request.method} {request.url} - Status {response.status_code}")

    def get_request(
        self, path: str, params: typing.Optional[QueryParamTypes] = None, silence_404: bool = False
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
            # /user/gpg_key_token returns text instead of JSON
            if "/user/gpg_key_token" in path:
                return self.RequestModel(response, response.text)
            return self.RequestModel(response, json.loads(response.text))

        return self.RequestModel(response, "")

    def post_request(
        self,
        path: str,
        error_400: str = "HTTP 400 Bad Request",
        error_403: str = "HTTP 403 Forbidden",
        error_404: str = "HTTP 404 Not Found",
        error_405: str = "HTTP 405 Method Not Allowed",
        error_409: str = "HTTP 409 Conflict",
        error_422: str = "HTTP 422 Unprocessable Entity",
    ):
        try:
            self.logger.debug(f"GET {path}")
            response: httpx.Response = self.client.get(self.url + path)
            response.raise_for_status()

        except httpx.RequestError as exc:
            error_msg = f"An error occurred while requesting {exc.request.url!r}."
            self.logger.error(error_msg)

        except httpx.HTTPStatusError as exc:

            # 400 Bad Request
            if exc.response.status_code == 400:
                self.logger.error(f"{error_400}")

            # 403 Forbidden
            elif exc.response.status_code == 403:
                self.logger.error(f"{error_403}")

            # 404 Not Found
            elif exc.response.status_code == 404:
                self.logger.error(f"{error_404}")

            # 405 Not Found
            elif exc.response.status_code == 405:
                self.logger.error(f"{error_405}")

            # 409 Conflict
            elif exc.response.status_code == 409:
                self.logger.error(f"{error_409}")

            # 422 Unprocessable Entity
            elif exc.response.status_code == 422:
                self.logger.error(f"{error_422}")

            else:
                self.logger.error(f"An error occurred while requesting {exc.request.url!r}.")

        if response.text:
            return self.RequestModel(response, json.loads(response.text))

        return self.RequestModel(response, "")

    def put_request(self):
        pass

    def delete_request(self):
        pass
