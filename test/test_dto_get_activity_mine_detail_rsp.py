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

from cnb_api.models.dto_get_activity_mine_detail_rsp import DtoGetActivityMineDetailRsp

class TestDtoGetActivityMineDetailRsp(unittest.TestCase):
    """DtoGetActivityMineDetailRsp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DtoGetActivityMineDetailRsp:
        """Test DtoGetActivityMineDetailRsp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DtoGetActivityMineDetailRsp`
        """
        model = DtoGetActivityMineDetailRsp()
        if include_optional:
            return DtoGetActivityMineDetailRsp(
                activity_mine_datas = [
                    cnb_api.models.dto/activity_mine_data.dto.ActivityMineData(
                        activity_type = 'mine', 
                        created_at = cnb_api.models.convert/null_time.convert.NullTime(
                            time = '', 
                            valid = True, ), 
                        repo = cnb_api.models.dto/activity_repos.dto.ActivityRepos(
                            description = '', 
                            display_module = 1, 
                            fork_count = 56, 
                            fork_target = '', 
                            forked_from = '', 
                            freeze = True, 
                            id = 56, 
                            is_star = True, 
                            language = '', 
                            last_updated_at = cnb_api.models.last_updated_at.last_updated_at(), 
                            license = '', 
                            mark_count = 56, 
                            name = '', 
                            path = '', 
                            site = '', 
                            star_count = 56, 
                            status = cnb_api.models.status.status(), 
                            topics = '', 
                            updated_at = '', 
                            visibility_level = 0, ), 
                        user = cnb_api.models.dto/activity_users.dto.ActivityUsers(
                            address = '', 
                            appreciate_status = 56, 
                            avatar = '', 
                            bio = '', 
                            company = '', 
                            email = '', 
                            follow_count = 56, 
                            follow_mission_count = 56, 
                            follow_repo_count = 56, 
                            follower_count = 56, 
                            freeze = True, 
                            gender = 56, 
                            group_count = 56, 
                            id = '', 
                            is_follow = True, 
                            location = '', 
                            mission_count = 56, 
                            nickname = '', 
                            registry_count = 56, 
                            repo_count = 56, 
                            reward_amount = 56, 
                            reward_count = 56, 
                            site = '', 
                            stars_count = 56, 
                            type = 0, 
                            username = '', 
                            verified = 56, 
                            verified_expire_in = '', 
                            wechat_mp = '', 
                            wechat_mp_qrcode = '', ), )
                    ],
                next_offset = ''
            )
        else:
            return DtoGetActivityMineDetailRsp(
        )
        """

    def testDtoGetActivityMineDetailRsp(self):
        """Test DtoGetActivityMineDetailRsp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
