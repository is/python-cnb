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

from cnb_api.models.web_update_lfs_quota_form import WebUpdateLfsQuotaForm

class TestWebUpdateLfsQuotaForm(unittest.TestCase):
    """WebUpdateLfsQuotaForm unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebUpdateLfsQuotaForm:
        """Test WebUpdateLfsQuotaForm
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebUpdateLfsQuotaForm`
        """
        model = WebUpdateLfsQuotaForm()
        if include_optional:
            return WebUpdateLfsQuotaForm(
                lfs_object_size_limit_in_kib = '',
                lfs_quota_in_kib = '',
                quota_in_kib = 56
            )
        else:
            return WebUpdateLfsQuotaForm(
        )
        """

    def testWebUpdateLfsQuotaForm(self):
        """Test WebUpdateLfsQuotaForm"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
