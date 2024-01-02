# coding: utf-8

"""
    Jupyter Server API

    Server API

    The version of the OpenAPI document: 5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from nbserv_client.api.sessions_api import SessionsApi


class TestSessionsApi(unittest.TestCase):
    """SessionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SessionsApi()

    def tearDown(self) -> None:
        pass

    def test_api_sessions_get(self) -> None:
        """Test case for api_sessions_get

        List available sessions
        """
        pass

    def test_api_sessions_post(self) -> None:
        """Test case for api_sessions_post

        Create a new session, or return an existing session if a session of the same name already exists
        """
        pass

    def test_api_sessions_session_delete(self) -> None:
        """Test case for api_sessions_session_delete

        Delete a session
        """
        pass

    def test_api_sessions_session_get(self) -> None:
        """Test case for api_sessions_session_get

        Get session
        """
        pass

    def test_api_sessions_session_patch(self) -> None:
        """Test case for api_sessions_session_patch

        This can be used to rename the session.
        """
        pass


if __name__ == '__main__':
    unittest.main()
