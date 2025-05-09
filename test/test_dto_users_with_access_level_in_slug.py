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

from cnb_api.models.dto_users_with_access_level_in_slug import DtoUsersWithAccessLevelInSlug

class TestDtoUsersWithAccessLevelInSlug(unittest.TestCase):
    """DtoUsersWithAccessLevelInSlug unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DtoUsersWithAccessLevelInSlug:
        """Test DtoUsersWithAccessLevelInSlug
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DtoUsersWithAccessLevelInSlug`
        """
        model = DtoUsersWithAccessLevelInSlug()
        if include_optional:
            return DtoUsersWithAccessLevelInSlug(
                access_level = 0,
                avatar = '',
                created_at = '',
                email = '',
                email_verification = '',
                freeze = True,
                id = '',
                inviter = cnb_api.models.dto/users.dto.Users(
                    avatar = '', 
                    created_at = '', 
                    email = '', 
                    freeze = True, 
                    id = '', 
                    nickname = '', 
                    type = 0, 
                    username = '', 
                    verified = 56, 
                    verified_expire_in = '', ),
                join_time = '',
                nickname = '',
                type = 0,
                username = '',
                verified = 56,
                verified_expire_in = ''
            )
        else:
            return DtoUsersWithAccessLevelInSlug(
        )
        """

    def testDtoUsersWithAccessLevelInSlug(self):
        """Test DtoUsersWithAccessLevelInSlug"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
