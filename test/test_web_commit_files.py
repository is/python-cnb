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

from cnb_api.models.web_commit_files import WebCommitFiles

class TestWebCommitFiles(unittest.TestCase):
    """WebCommitFiles unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebCommitFiles:
        """Test WebCommitFiles
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebCommitFiles`
        """
        model = WebCommitFiles()
        if include_optional:
            return WebCommitFiles(
                base_commit = '',
                diff = cnb_api.models.web/diff.web.Diff(
                    base_commit = '', 
                    file_exceeded = True, 
                    file_limit = 56, 
                    files = [
                        cnb_api.models.web/diff_file.web.DiffFile(
                            change_type = '', 
                            deletions = 56, 
                            file_index = 56, 
                            insertions = 56, 
                            is_bin = True, 
                            old_path = '', 
                            path = '', 
                            sections = [
                                cnb_api.models.web/diff_section.web.DiffSection(
                                    lines = [
                                        cnb_api.models.web/diff_line.web.DiffLine(
                                            content = '', 
                                            left_line_number = 56, 
                                            prefix = '', 
                                            right_line_number = 56, 
                                            type = '', )
                                        ], )
                                ], )
                        ], 
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
                straight = True
            )
        else:
            return WebCommitFiles(
        )
        """

    def testWebCommitFiles(self):
        """Test WebCommitFiles"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
