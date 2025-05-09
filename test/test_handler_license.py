# coding: utf-8

"""
    CNB OPENAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Contact: cnb@tencent.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cnb_api.models.handler_license import HandlerLicense

class TestHandlerLicense(unittest.TestCase):
    """HandlerLicense unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HandlerLicense:
        """Test HandlerLicense
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HandlerLicense`
        """
        model = HandlerLicense()
        if include_optional:
            return HandlerLicense(
                body = '',
                conditions = [
                    ''
                    ],
                description = '',
                key = '',
                limitations = [
                    ''
                    ],
                name = '',
                permissions = [
                    ''
                    ],
                spdx_id = ''
            )
        else:
            return HandlerLicense(
        )
        """

    def testHandlerLicense(self):
        """Test HandlerLicense"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
