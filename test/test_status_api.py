# coding: utf-8

"""
    Jupyter Server API

    Server API

    The version of the OpenAPI document: 5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from nbserv_client.api.status_api import StatusApi


class TestStatusApi(unittest.TestCase):
    """StatusApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StatusApi()

    def tearDown(self) -> None:
        pass

    def test_api_status_get(self) -> None:
        """Test case for api_status_get

        Get the current status/activity of the server.
        """
        pass


if __name__ == '__main__':
    unittest.main()
