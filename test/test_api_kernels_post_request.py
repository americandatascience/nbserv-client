# coding: utf-8

"""
    Jupyter Server API

    Server API

    The version of the OpenAPI document: 5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.api_kernels_post_request import ApiKernelsPostRequest

class TestApiKernelsPostRequest(unittest.TestCase):
    """ApiKernelsPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiKernelsPostRequest:
        """Test ApiKernelsPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiKernelsPostRequest`
        """
        model = ApiKernelsPostRequest()
        if include_optional:
            return ApiKernelsPostRequest(
                name = '',
                path = ''
            )
        else:
            return ApiKernelsPostRequest(
                name = '',
        )
        """

    def testApiKernelsPostRequest(self):
        """Test ApiKernelsPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()