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

from openapi_client.models.session import Session

class TestSession(unittest.TestCase):
    """Session unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Session:
        """Test Session
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Session`
        """
        model = Session()
        if include_optional:
            return Session(
                id = '',
                path = '',
                name = '',
                type = '',
                kernel = openapi_client.models.kernel.Kernel(
                    id = '', 
                    name = '', 
                    last_activity = '', 
                    connections = 1.337, 
                    execution_state = '', )
            )
        else:
            return Session(
        )
        """

    def testSession(self):
        """Test Session"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()