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

from cnb_api.models.dto_repo_rank import DtoRepoRank

class TestDtoRepoRank(unittest.TestCase):
    """DtoRepoRank unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DtoRepoRank:
        """Test DtoRepoRank
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DtoRepoRank`
        """
        model = DtoRepoRank()
        if include_optional:
            return DtoRepoRank(
                rank_type = '',
                repo_detail = [
                    cnb_api.models.dto/rank_detail.dto.RankDetail(
                        created_at = '', 
                        description = '', 
                        display_module = 1, 
                        fork_count = 56, 
                        forked_from_repo = cnb_api.models.forked_from_repo.forked_from_repo(), 
                        freeze = True, 
                        id = 56, 
                        language = '', 
                        languages = cnb_api.models.languages.languages(), 
                        last_update_nickname = '', 
                        last_update_username = '', 
                        last_updated_at = cnb_api.models.last_updated_at.last_updated_at(), 
                        license = '', 
                        mark_count = 56, 
                        name = '', 
                        open_issue_count = 56, 
                        open_pull_request_count = 56, 
                        path = '', 
                        rank_value = 56, 
                        site = '', 
                        star_count = 56, 
                        status = cnb_api.models.status.status(), 
                        tags = [
                            cnb_api.models.dto_rank_detail_tags_inner.dto_RankDetail_tags_inner(
                                name = '', )
                            ], 
                        topics = '', 
                        updated_at = '', 
                        visibility_level = 0, 
                        web_url = '', )
                    ],
                top_n = 56
            )
        else:
            return DtoRepoRank(
        )
        """

    def testDtoRepoRank(self):
        """Test DtoRepoRank"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
