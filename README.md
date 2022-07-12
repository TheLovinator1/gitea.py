# gitea.py

An API wrapper for Gitea written in Python.

## Work in progress

This API wrapper is still in development. It is not yet complete, and it is not yet ready for use and it will break without warning, so you should wait for the v1.0.0 release.

## Tests

You need environment variables to run the tests:

| Environment Variable | Description                                                                                |
| -------------------- | ------------------------------------------------------------------------------------------ |
| `GITEA_URL`          | The URL of the Gitea instance to test against. (For example: https://git.lovinator.space ) |
| `GITEA_TOKEN`        | Settings -> Applications -> Create Token                                                   |

The tests expect that you have a user named "LoviBot" that we are following.

There is also an `testboi.py` file in the root directory that can be used to test the API. This has print statements that can be used to debug the API.

## Need help?

- Email: [tlovinator@gmail.com](mailto:tlovinator@gmail.com)
- Discord: TheLovinator#9276
- Send an issue: [GitHub](https://github.com/TheLovinator1/gitea.py/issues) | [Gitea](https://git.lovinator.space/TheLovinator/gitea.py/issues)
