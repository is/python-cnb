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

from cnb_api.models.web_commit_object import WebCommitObject

class TestWebCommitObject(unittest.TestCase):
    """WebCommitObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebCommitObject:
        """Test WebCommitObject
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebCommitObject`
        """
        model = WebCommitObject()
        if include_optional:
            return WebCommitObject(
                author = cnb_api.models.web/signature.web.Signature(
                    date = '', 
                    email = '', 
                    name = '', ),
                comment_count = 56,
                committer = cnb_api.models.web/signature.web.Signature(
                    date = '', 
                    email = '', 
                    name = '', ),
                message = '',
                tree = cnb_api.models.web/commit_object_tree.web.CommitObjectTree(
                    sha = '', ),
                verification = cnb_api.models.web/commit_object_verification.web.CommitObjectVerification(
                    payload = '', 
                    reason = '', 
                    signature = '', 
                    verified = True, )
            )
        else:
            return WebCommitObject(
        )
        """

    def testWebCommitObject(self):
        """Test WebCommitObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
