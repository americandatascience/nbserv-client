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

from openapi_client.models.kernel_spec_resources import KernelSpecResources

class TestKernelSpecResources(unittest.TestCase):
    """KernelSpecResources unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> KernelSpecResources:
        """Test KernelSpecResources
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `KernelSpecResources`
        """
        model = KernelSpecResources()
        if include_optional:
            return KernelSpecResources(
                kernel_js = '',
                kernel_css = '',
                logo_ = ''
            )
        else:
            return KernelSpecResources(
        )
        """

    def testKernelSpecResources(self):
        """Test KernelSpecResources"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()