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

from cnb_api.models.web_issue_summary import WebIssueSummary

class TestWebIssueSummary(unittest.TestCase):
    """WebIssueSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebIssueSummary:
        """Test WebIssueSummary
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebIssueSummary`
        """
        model = WebIssueSummary()
        if include_optional:
            return WebIssueSummary(
                closed_issue_number = 56,
                closed_pull_request_number = 56,
                open_issue_number = 56,
                open_pull_request_number = 56
            )
        else:
            return WebIssueSummary(
        )
        """

    def testWebIssueSummary(self):
        """Test WebIssueSummary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
