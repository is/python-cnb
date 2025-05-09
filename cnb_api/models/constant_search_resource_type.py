# coding: utf-8

"""
    CNB OPENAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Contact: cnb@tencent.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ConstantSearchResourceType(int, Enum):
    """
    ConstantSearchResourceType
    """

    """
    allowed enum values
    """
    All = 0
    Group = 1
    Repo = 2
    User = 3
    Release = 4
    PullRequest = 5

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ConstantSearchResourceType from a JSON string"""
        return cls(json.loads(json_str))


