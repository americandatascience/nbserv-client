# coding: utf-8

"""
    Jupyter Server API

    Server API

    The version of the OpenAPI document: 5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from nbserv_client.api.identity_api import IdentityApi


class TestIdentityApi(unittest.TestCase):
    """IdentityApi unit test stubs"""

    def setUp(self) -> None:
        self.api = IdentityApi()

    def tearDown(self) -> None:
        pass

    def test_api_me_get(self) -> None:
        """Test case for api_me_get

        Get the identity of the currently authenticated user. If present, a `permissions` argument may be specified to check what actions the user currently is authorized to take. 
        """
        pass


if __name__ == '__main__':
    unittest.main()
