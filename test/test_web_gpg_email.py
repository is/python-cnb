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

from cnb_api.models.web_gpg_email import WebGPGEmail

class TestWebGPGEmail(unittest.TestCase):
    """WebGPGEmail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebGPGEmail:
        """Test WebGPGEmail
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebGPGEmail`
        """
        model = WebGPGEmail()
        if include_optional:
            return WebGPGEmail(
                email = '',
                verified = True
            )
        else:
            return WebGPGEmail(
        )
        """

    def testWebGPGEmail(self):
        """Test WebGPGEmail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
