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

from openapi_client.models.api_contents_path_get400_response import ApiContentsPathGet400Response

class TestApiContentsPathGet400Response(unittest.TestCase):
    """ApiContentsPathGet400Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiContentsPathGet400Response:
        """Test ApiContentsPathGet400Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiContentsPathGet400Response`
        """
        model = ApiContentsPathGet400Response()
        if include_optional:
            return ApiContentsPathGet400Response(
                error = '',
                reason = ''
            )
        else:
            return ApiContentsPathGet400Response(
        )
        """

    def testApiContentsPathGet400Response(self):
        """Test ApiContentsPathGet400Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()