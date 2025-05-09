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

from cnb_api.api.organizations_api import OrganizationsApi


class TestOrganizationsApi(unittest.TestCase):
    """OrganizationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OrganizationsApi()

    def tearDown(self) -> None:
        pass

    def test_create_organization(self) -> None:
        """Test case for create_organization

        创建新组织。Create new organization.
        """
        pass

    def test_delete_organization(self) -> None:
        """Test case for delete_organization

        删除指定组织。Delete the specified organization.
        """
        pass

    def test_get_group(self) -> None:
        """Test case for get_group

        获取指定组织信息。Get information for the specified organization.
        """
        pass

    def test_get_group_setting(self) -> None:
        """Test case for get_group_setting

        获取指定组织的配置详情。Get the configuration details for the specified organization.
        """
        pass

    def test_get_groups_by_user_id(self) -> None:
        """Test case for get_groups_by_user_id

        获取指定用户拥有权限的顶层组织列表。 Get a list of top-level organizations that the specified user has permissions to access.
        """
        pass

    def test_list_groups(self) -> None:
        """Test case for list_groups

        查询当前用户在指定组织下拥有指定权限的子组织列表。Get the list of sub-organizations that the current user has access to in the specified organization.
        """
        pass

    def test_list_subgroups(self) -> None:
        """Test case for list_subgroups

        获取指定组织下的子组织列表。Get the list of sub-organizations under the specified organization.
        """
        pass

    def test_list_top_groups(self) -> None:
        """Test case for list_top_groups

        获取当前用户拥有权限的顶层组织列表。Get top-level organizations list that the current user has access to.
        """
        pass

    def test_update_group_avatar(self) -> None:
        """Test case for update_group_avatar

        更新组织头像 URL 地址。Updates the organization avatar URL.
        """
        pass

    def test_update_group_setting(self) -> None:
        """Test case for update_group_setting

        更新指定组织的配置。Updates the configuration for the specified organization.
        """
        pass

    def test_update_organization(self) -> None:
        """Test case for update_organization

        更新组织信息, 可更新的内容为: 组织描述, 组织展示名称, 组织网站, 组织联系邮箱。Updates organization information including: description, display name, website URL and contact email.
        """
        pass


if __name__ == '__main__':
    unittest.main()
