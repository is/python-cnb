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

from cnb_api.models.openapi_commit_asset_upload_url import OpenapiCommitAssetUploadURL

class TestOpenapiCommitAssetUploadURL(unittest.TestCase):
    """OpenapiCommitAssetUploadURL unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OpenapiCommitAssetUploadURL:
        """Test OpenapiCommitAssetUploadURL
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OpenapiCommitAssetUploadURL`
        """
        model = OpenapiCommitAssetUploadURL()
        if include_optional:
            return OpenapiCommitAssetUploadURL(
                expires_in_sec = 56,
                upload_url = '',
                verify_url = ''
            )
        else:
            return OpenapiCommitAssetUploadURL(
        )
        """

    def testOpenapiCommitAssetUploadURL(self):
        """Test OpenapiCommitAssetUploadURL"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
