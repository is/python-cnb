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

from cnb_api.models.dto_container_image import DtoContainerImage

class TestDtoContainerImage(unittest.TestCase):
    """DtoContainerImage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DtoContainerImage:
        """Test DtoContainerImage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DtoContainerImage`
        """
        model = DtoContainerImage()
        if include_optional:
            return DtoContainerImage(
                arch = '',
                digest = '',
                layers = [
                    cnb_api.models.dto/container_image_layer.dto.ContainerImageLayer(
                        instruction = '', 
                        size = 56, )
                    ],
                os = '',
                size = 56
            )
        else:
            return DtoContainerImage(
        )
        """

    def testDtoContainerImage(self):
        """Test DtoContainerImage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
