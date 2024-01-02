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

from nbserv_client.models.kernel_spec import KernelSpec

class TestKernelSpec(unittest.TestCase):
    """KernelSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> KernelSpec:
        """Test KernelSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `KernelSpec`
        """
        model = KernelSpec()
        if include_optional:
            return KernelSpec(
                name = '',
                kernel_spec_file = nbserv_client.models.kernel_spec_file.KernelSpecFile(
                    language = '', 
                    argv = [
                        ''
                        ], 
                    display_name = '', 
                    codemirror_mode = '', 
                    env = {
                        'key' : ''
                        }, 
                    help_links = [
                        nbserv_client.models.kernel_spec_file_help_links_inner.KernelSpecFile_help_links_inner(
                            text = '', 
                            url = '', )
                        ], ),
                resources = nbserv_client.models.kernel_spec_resources.KernelSpec_resources(
                    kernel/js = '', 
                    kernel/css = '', 
                    logo_* = '', )
            )
        else:
            return KernelSpec(
        )
        """

    def testKernelSpec(self):
        """Test KernelSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
