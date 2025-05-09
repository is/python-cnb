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

from cnb_api.models.web_tree_content import WebTreeContent

class TestWebTreeContent(unittest.TestCase):
    """WebTreeContent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebTreeContent:
        """Test WebTreeContent
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebTreeContent`
        """
        model = WebTreeContent()
        if include_optional:
            return WebTreeContent(
                branch_count = 56,
                cnb_settings = cnb_api.models.web/preload_file.web.PreloadFile(
                    content = '', 
                    encoding = '', 
                    file_stat = cnb_api.models.web/file_stat.web.FileStat(
                        mime_type = cnb_api.models.web/mime_type.web.MIMEType(
                            content_type = '', 
                            externsion = '', 
                            is_audio = True, 
                            is_browsable_binary_type = True, 
                            is_image = True, 
                            is_pdf = True, 
                            is_representable_as_text = True, 
                            is_svg_image = True, 
                            is_text = True, 
                            is_video = True, ), ), 
                    name = '', ),
                commit_count = 56,
                commit_count_exceeded = True,
                entries = [
                    cnb_api.models.web/tree_entry.web.TreeEntry(
                        is_lfs = True, 
                        name = '', 
                        path = '', 
                        sha = '', 
                        submodule = cnb_api.models.web/submodule.web.Submodule(
                            link_url = '', ), 
                        type = '', )
                    ],
                file_list_exceeded = True,
                file_list_limit = 56,
                has_web_trigger = True,
                initialized = True,
                is_protected = True,
                last_commit = cnb_api.models.web/commit.web.Commit(
                    author = cnb_api.models.git_woa_com_cnb_monorepo_git_internal_app_git_service_bff_web/user_info.git_woa_com_cnb_monorepo_git_internal_app_git_service_bff_web.UserInfo(
                        freeze = True, 
                        nickname = '', 
                        username = '', ), 
                    commit = cnb_api.models.web/commit_object.web.CommitObject(
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
                            verified = True, ), ), 
                    commit_statuses = cnb_api.models.web/commit_statuses.web.CommitStatuses(
                        sha = '', 
                        state = '', 
                        statuses = [
                            cnb_api.models.web/commit_status.web.CommitStatus(
                                context = '', 
                                created_at = '', 
                                description = '', 
                                state = '', 
                                target_url = '', 
                                updated_at = '', )
                            ], ), 
                    committer = cnb_api.models.git_woa_com_cnb_monorepo_git_internal_app_git_service_bff_web/user_info.git_woa_com_cnb_monorepo_git_internal_app_git_service_bff_web.UserInfo(
                        freeze = True, 
                        nickname = '', 
                        username = '', ), 
                    files = cnb_api.models.web/commit_files.web.CommitFiles(
                        base_commit = '', 
                        diff = cnb_api.models.web/diff.web.Diff(
                            base_commit = '', 
                            file_exceeded = True, 
                            file_limit = 56, 
                            head_commit = '', 
                            stat = cnb_api.models.web/diff_stat.web.DiffStat(
                                deletions = 56, 
                                entry_exceeded = True, 
                                entry_limit = 56, 
                                insertions = 56, 
                                paths = [
                                    cnb_api.models.web/diff_entry.web.DiffEntry(
                                        change_type = '', 
                                        deletions = 56, 
                                        file_index = 56, 
                                        insertions = 56, 
                                        is_bin = True, 
                                        old_path = '', 
                                        path = '', )
                                    ], ), ), 
                        head_commit = '', 
                        straight = True, ), 
                    parents = [
                        cnb_api.models.web/commit_parent.web.CommitParent(
                            sha = '', )
                        ], 
                    sha = '', ),
                name = '',
                path = '',
                read_me = cnb_api.models.web/preload_file.web.PreloadFile(
                    content = '', 
                    encoding = '', 
                    file_stat = cnb_api.models.web/file_stat.web.FileStat(
                        mime_type = cnb_api.models.web/mime_type.web.MIMEType(
                            content_type = '', 
                            externsion = '', 
                            is_audio = True, 
                            is_browsable_binary_type = True, 
                            is_image = True, 
                            is_pdf = True, 
                            is_representable_as_text = True, 
                            is_svg_image = True, 
                            is_text = True, 
                            is_video = True, ), ), 
                    name = '', ),
                repository = cnb_api.models.web/repository.web.Repository(
                    head_ref = '', 
                    http_clone_url = '', 
                    slug = '', 
                    ssh_clone_url = '', 
                    usage = cnb_api.models.web/repository_usage.web.RepositoryUsage(
                        git_size_in_kib = '', 
                        lfs_size_in_kib = '', ), ),
                tag_count = 56,
                type = ''
            )
        else:
            return WebTreeContent(
        )
        """

    def testWebTreeContent(self):
        """Test WebTreeContent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
