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

from cnb_api.models.web_pull_request_review_comment import WebPullRequestReviewComment

class TestWebPullRequestReviewComment(unittest.TestCase):
    """WebPullRequestReviewComment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebPullRequestReviewComment:
        """Test WebPullRequestReviewComment
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebPullRequestReviewComment`
        """
        model = WebPullRequestReviewComment()
        if include_optional:
            return WebPullRequestReviewComment(
                author = cnb_api.models.git_woa_com_cnb_monorepo_git_internal_dto_web/user_info.git_woa_com_cnb_monorepo_git_internal_dto_web.UserInfo(
                    freeze = True, 
                    nickname = '', 
                    username = '', ),
                author_meta = [
                    56
                    ],
                body = '',
                comment_id = '',
                commit_hash = '',
                created_at = '',
                diff_hunk = [
                    cnb_api.models.web/diff_line.web.DiffLine(
                        content = '', 
                        left_line_number = 56, 
                        prefix = '', 
                        right_line_number = 56, 
                        type = '', )
                    ],
                end_line = 56,
                end_side = '',
                path = '',
                replies = [
                    cnb_api.models.web/pull_request_review_comment_reply.web.PullRequestReviewCommentReply(
                        author = cnb_api.models.git_woa_com_cnb_monorepo_git_internal_dto_web/user_info.git_woa_com_cnb_monorepo_git_internal_dto_web.UserInfo(
                            freeze = True, 
                            nickname = '', 
                            username = '', ), 
                        body = '', 
                        comment_id = '', 
                        created_at = '', 
                        updated_at = '', )
                    ],
                reply_to_comment_id = '',
                review_id = '',
                start_line = 56,
                start_side = '',
                subject_type = '',
                updated_at = ''
            )
        else:
            return WebPullRequestReviewComment(
        )
        """

    def testWebPullRequestReviewComment(self):
        """Test WebPullRequestReviewComment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
