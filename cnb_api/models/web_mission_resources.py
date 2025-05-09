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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from cnb_api.models.web_issue_resource import WebIssueResource
from cnb_api.models.web_pull_request_resource import WebPullRequestResource
from typing import Optional, Set
from typing_extensions import Self

class WebMissionResources(BaseModel):
    """
    WebMissionResources
    """ # noqa: E501
    issues: Optional[List[WebIssueResource]] = None
    pull_requests: Optional[List[WebPullRequestResource]] = None
    __properties: ClassVar[List[str]] = ["issues", "pull_requests"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of WebMissionResources from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in issues (list)
        _items = []
        if self.issues:
            for _item_issues in self.issues:
                if _item_issues:
                    _items.append(_item_issues.to_dict())
            _dict['issues'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in pull_requests (list)
        _items = []
        if self.pull_requests:
            for _item_pull_requests in self.pull_requests:
                if _item_pull_requests:
                    _items.append(_item_pull_requests.to_dict())
            _dict['pull_requests'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebMissionResources from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "issues": [WebIssueResource.from_dict(_item) for _item in obj["issues"]] if obj.get("issues") is not None else None,
            "pull_requests": [WebPullRequestResource.from_dict(_item) for _item in obj["pull_requests"]] if obj.get("pull_requests") is not None else None
        })
        return _obj


