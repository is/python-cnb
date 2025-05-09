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

from cnb_api.models.dto_access_token_item import DtoAccessTokenItem

class TestDtoAccessTokenItem(unittest.TestCase):
    """DtoAccessTokenItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DtoAccessTokenItem:
        """Test DtoAccessTokenItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DtoAccessTokenItem`
        """
        model = DtoAccessTokenItem()
        if include_optional:
            return DtoAccessTokenItem(
                created_at = '',
                description = '',
                expired_at = '',
                last_activity_at = '',
                resource_type = 0,
                scope = '',
                slug = '',
                title = '',
                token_fragment = '',
                token_id = ''
            )
        else:
            return DtoAccessTokenItem(
        )
        """

    def testDtoAccessTokenItem(self):
        """Test DtoAccessTokenItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
