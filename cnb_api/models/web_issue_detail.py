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

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cnb_api.models.git_woa_com_cnb_monorepo_git_internal_dto_web_user_info import GitWoaComCnbMonorepoGitInternalDtoWebUserInfo
from cnb_api.models.label_option import LabelOption
from cnb_api.models.web_issue_assignee import WebIssueAssignee
from typing import Optional, Set
from typing_extensions import Self

class WebIssueDetail(BaseModel):
    """
    WebIssueDetail
    """ # noqa: E501
    assignees: Optional[List[WebIssueAssignee]] = None
    author: Optional[GitWoaComCnbMonorepoGitInternalDtoWebUserInfo] = None
    body: Optional[StrictStr] = None
    comment_count: Optional[StrictInt] = None
    created_at: Optional[StrictStr] = None
    ended_at: Optional[StrictStr] = None
    labels: Optional[List[LabelOption]] = None
    last_acted_at: Optional[StrictStr] = None
    number: Optional[StrictStr] = None
    participants: Optional[List[GitWoaComCnbMonorepoGitInternalDtoWebUserInfo]] = None
    priority: Optional[StrictStr] = None
    started_at: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    state_reason: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["assignees", "author", "body", "comment_count", "created_at", "ended_at", "labels", "last_acted_at", "number", "participants", "priority", "started_at", "state", "state_reason", "title", "updated_at"]

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
        """Create an instance of WebIssueDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in assignees (list)
        _items = []
        if self.assignees:
            for _item_assignees in self.assignees:
                if _item_assignees:
                    _items.append(_item_assignees.to_dict())
            _dict['assignees'] = _items
        # override the default output from pydantic by calling `to_dict()` of author
        if self.author:
            _dict['author'] = self.author.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in labels (list)
        _items = []
        if self.labels:
            for _item_labels in self.labels:
                if _item_labels:
                    _items.append(_item_labels.to_dict())
            _dict['labels'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in participants (list)
        _items = []
        if self.participants:
            for _item_participants in self.participants:
                if _item_participants:
                    _items.append(_item_participants.to_dict())
            _dict['participants'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebIssueDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assignees": [WebIssueAssignee.from_dict(_item) for _item in obj["assignees"]] if obj.get("assignees") is not None else None,
            "author": GitWoaComCnbMonorepoGitInternalDtoWebUserInfo.from_dict(obj["author"]) if obj.get("author") is not None else None,
            "body": obj.get("body"),
            "comment_count": obj.get("comment_count"),
            "created_at": obj.get("created_at"),
            "ended_at": obj.get("ended_at"),
            "labels": [LabelOption.from_dict(_item) for _item in obj["labels"]] if obj.get("labels") is not None else None,
            "last_acted_at": obj.get("last_acted_at"),
            "number": obj.get("number"),
            "participants": [GitWoaComCnbMonorepoGitInternalDtoWebUserInfo.from_dict(_item) for _item in obj["participants"]] if obj.get("participants") is not None else None,
            "priority": obj.get("priority"),
            "started_at": obj.get("started_at"),
            "state": obj.get("state"),
            "state_reason": obj.get("state_reason"),
            "title": obj.get("title"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


