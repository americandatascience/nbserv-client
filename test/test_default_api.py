# coding: utf-8

"""
    Jupyter Server API

    Server API

    The version of the OpenAPI document: 5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from nbserv_client.api.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DefaultApi()

    def tearDown(self) -> None:
        pass

    def test_api_get(self) -> None:
        """Test case for api_get

        Get the Jupyter Server version
        """
        pass


if __name__ == '__main__':
    unittest.main()
