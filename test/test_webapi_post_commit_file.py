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

from cnb_api.models.webapi_post_commit_file import WebapiPostCommitFile

class TestWebapiPostCommitFile(unittest.TestCase):
    """WebapiPostCommitFile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebapiPostCommitFile:
        """Test WebapiPostCommitFile
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebapiPostCommitFile`
        """
        model = WebapiPostCommitFile()
        if include_optional:
            return WebapiPostCommitFile(
                content = '',
                encoding = '',
                is_deleted = True,
                is_executable = True,
                path = ''
            )
        else:
            return WebapiPostCommitFile(
        )
        """

    def testWebapiPostCommitFile(self):
        """Test WebapiPostCommitFile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
