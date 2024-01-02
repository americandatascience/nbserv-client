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

from openapi_client.models.api_me_get200_response import ApiMeGet200Response

class TestApiMeGet200Response(unittest.TestCase):
    """ApiMeGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiMeGet200Response:
        """Test ApiMeGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiMeGet200Response`
        """
        model = ApiMeGet200Response()
        if include_optional:
            return ApiMeGet200Response(
                identity = openapi_client.models.identity.Identity(
                    username = '', 
                    name = '', 
                    display_name = '', 
                    initials = '', 
                    avatar_url = '', 
                    color = '', ),
                permissions = {
                    'key' : [
                        ''
                        ]
                    }
            )
        else:
            return ApiMeGet200Response(
        )
        """

    def testApiMeGet200Response(self):
        """Test ApiMeGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
