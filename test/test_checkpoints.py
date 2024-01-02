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

from openapi_client.models.checkpoints import Checkpoints

class TestCheckpoints(unittest.TestCase):
    """Checkpoints unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Checkpoints:
        """Test Checkpoints
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Checkpoints`
        """
        model = Checkpoints()
        if include_optional:
            return Checkpoints(
                id = '',
                last_modified = ''
            )
        else:
            return Checkpoints(
                id = '',
                last_modified = '',
        )
        """

    def testCheckpoints(self):
        """Test Checkpoints"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()